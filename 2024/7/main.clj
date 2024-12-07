(require '[clojure.string :as str])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(defn parse-line [line]
  (let [parts (str/split line #": ")
        target (Integer/parseInt (first parts))
        nums (mapv Integer/parseInt (str/split (second parts) #" "))]
    [target nums]))

(defn generate-arrangements [num-slots options]
  (if (zero? num-slots)
    '(())
    (for [arrangement (generate-arrangements (dec num-slots) options)
          option options]
      (conj arrangement option))))

(defn calc-vals [ops equations]
  (map (fn [[target nums]]
         (mapv (fn [op-ords]
                 (let [val (reduce (fn [acc [num op]]
                                     (case op
                                       0 (+ acc num)
                                       1 (* acc num)
                                       2 (Integer/parseInt (str acc num))))
                                   (first nums)
                                   (map vector (rest nums) op-ords))]
                   (if (= val target)
                     val
                     nil)))
               (generate-arrangements (dec (count nums)) ops))) equations))

(println (->> (map parse-line lines)
              (calc-vals [0 1])
              (map #(some identity %))
              (filter some?)
              (reduce +)))

(println (->>  (map parse-line lines)
               (calc-vals [0 1 2])
               (map #(some identity %))
               (filter some?)
               (reduce +)))
