(require '[clojure.string :as str])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(def disk-map (mapv #(Character/digit % 10) (first lines)))

(defn rpt-vec [v n] (vec (repeat n v)))

(defn checksum [disk]
  (reduce + (map-indexed (fn [i val] (if (>= val 0) (* i val) 0)) disk)))

(let [[disk files frees files2 frees2] (loop [disk []
                                              cur 0
                                              is-file true
                                              files []
                                              frees []
                                              files2 []
                                              frees2 []
                                              disk-map disk-map]
                                         (if (empty? disk-map)
                                           [disk files frees files2 frees2]
                                           (if is-file
                                             (let [length (first disk-map)
                                                   files' (concat files (vec (range (count disk) (+ (count disk) length))))
                                                   files2' (conj files2 [(count disk) length])
                                                   disk' (concat disk (rpt-vec cur length))]
                                               (recur disk' (inc cur) (not is-file) files' frees files2' frees2 (rest disk-map)))
                                             (let [length (first disk-map)
                                                   frees' (concat frees (vec (range (count disk) (+ (count disk) length))))
                                                   frees2' (conj frees2 [(count disk) length])
                                                   disk' (concat disk (rpt-vec -1 length))]
                                               (recur disk' cur (not is-file) files frees' files2 frees2' (rest disk-map))))))]

  (def disk1 (loop [disk (vec disk)
                    frees frees
                    files files]
               (if (> (first frees) (last files))
                 disk
                 (let [file-idx (last files)
                       free-idx (first frees)
                       disk' (assoc disk
                                    file-idx (disk free-idx)
                                    free-idx (disk file-idx))]
                   (recur disk' (rest frees) (butlast files))))))

  (def disk2 (first (reduce
                     (fn [[disk frees2] [file-idx file-len]]
                       (reduce
                        (fn [[disk frees2 broke] [i [free-idx free-len]]]
                          (if (and (<= file-len free-len) (> file-idx free-idx) (not broke))
                            (let [disk' (reduce
                                         (fn [disk j]
                                           (assoc (vec disk)
                                                  (+ free-idx j) ((vec disk) (+ file-idx j))
                                                  (+ file-idx j) ((vec disk) (+ free-idx j))))
                                         disk
                                         (range file-len))
                                  frees2' (assoc frees2 i [(+ free-idx file-len) (- free-len file-len)])]
                              [disk' frees2' true])
                            [disk frees2 broke]))
                        [disk frees2 false]
                        (map-indexed vector frees2)))
                     [disk frees2]
                     (reverse files2)))))

(println (checksum disk1))
(println (checksum disk2))