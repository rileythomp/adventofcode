(require '[clojure.string :as str])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(defn parse-line [line]
  (let [parts (str/split line #": ")
        target (Integer/parseInt (first parts))
        nums (map Integer/parseInt (str/split (second parts) #" "))]
    [target nums]))

(defn generate-arrangements [num-slots options]
  (if (zero? num-slots)
    '(())
    (for [arrangement (generate-arrangements (dec num-slots) options)
          option options]
      (conj arrangement option))))

(defn calc-num [cur [num op]]
  (case op
    0 (+ cur num)
    1 (* cur num)
    2 (Integer/parseInt (str cur num))))

(defn calc-val [target nums op-ords]
  (let [val (reduce calc-num
                    (first nums)
                    (map vector (rest nums) op-ords))]
    (if (= val target)
      val
      nil)))

(defn calc-ops [ops [target nums]]
  (map #(calc-val target nums %)
       (generate-arrangements (dec (count nums)) ops)))

(defn check-equations [lines, ops]
  (->> (map parse-line lines)
       (map #(calc-ops ops %))
       (map #(some identity %))
       (filter some?)
       (reduce +)))

(println (check-equations lines [0 1]))

(println (check-equations lines [0 1 2]))
