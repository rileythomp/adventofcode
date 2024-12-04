(require '[clojure.string :as str])

(defn ordered? [nums]
  (or (= nums (sort nums)) (= nums (sort > nums))))

(defn adjacent-diff? [nums]
  (->> (map #(abs (- %1 %2)) (rest nums) nums)
       (every? #{1 2 3})))

(defn is-safe? [nums]
  (and (ordered? nums) (adjacent-diff? nums)))

(defn remove-each [nums]
  (map-indexed
   (fn [idx _]
     (concat (take idx nums) (drop (inc idx) nums)))
   nums))

(def data (->> (slurp "in.txt")
               str/split-lines
               (map (fn [line] (map #(Integer/parseInt %) (str/split line #" "))))))

(println (count (filter is-safe? data)))
(println (count (filter #(some is-safe? (remove-each %)) data)))