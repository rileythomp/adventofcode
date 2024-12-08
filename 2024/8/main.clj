(require '[clojure.string :as str])
(require '[clojure.math.combinatorics :as combo])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(def grid (mapv (fn [line] (into [] line)) lines))

(def freqs (reduce (fn [acc [y row]]
                     (reduce (fn [acc [x cell]]
                               (if (not= cell \.)
                                 (update acc cell (fnil conj []) [y x])
                                 acc))
                             acc
                             (map-indexed vector row)))
                   {}
                   (map-indexed vector grid)))

(defn in-bounds? [y x]
  (and (>= y 0) (< y (count grid))
       (>= x 0) (< x (count (grid 0)))))

(defn add-obstacles [seen [oy1 ox1 oy2 ox2]]
  (cond-> seen
    (in-bounds? oy1 ox1) (conj [oy1 ox1])
    (in-bounds? oy2 ox2) (conj [oy2 ox2])))

(defn get-obstacles [y1 x1 y2 x2 dy dx]
  [(- y1 dy) (- x1 dx) (+ y2 dy) (+ x2 dx)])

(def ans (->> freqs
              (reduce-kv (fn [seen _ coords]
                           (let [pairs (combo/combinations coords 2)]
                             (reduce (fn [seen [[y1 x1] [y2 x2]]]
                                       (add-obstacles seen
                                                      (get-obstacles y1 x1 y2 x2 (- y2 y1) (- x2 x1))))
                                     seen
                                     pairs)))
                         #{})
              count))

(def ans2 (->> freqs
               (reduce-kv (fn [seen _ coords]
                            (let [pairs (combo/combinations coords 2)]
                              (reduce (fn [seen [[y1 x1] [y2 x2]]]
                                        (let [dy (- y2 y1) dx (- x2 x1)]
                                          (loop [seen (conj seen [y1 x1] [y2 x2])
                                                 [oy1 ox1 oy2 ox2] (get-obstacles y1 x1 y2 x2 dy dx)]
                                            (if (or (in-bounds? oy1 ox1)
                                                    (in-bounds? oy2 ox2))
                                              (recur (add-obstacles seen [oy1 ox1 oy2 ox2])
                                                     (get-obstacles oy1 ox1 oy2 ox2 dy dx))
                                              seen))))
                                      seen
                                      pairs)))
                          #{})
               count))

(println ans)
(println ans2)