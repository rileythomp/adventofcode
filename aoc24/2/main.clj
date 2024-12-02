(require '[clojure.string :as str])

(defn ordered? [coll]
  (or (= coll (sort coll))
      (= coll (sort > coll))))

(defn adjacent-diff? [nums]
  (every? #(and (>= % 1) (<= % 3)) (map #(abs (- %1 %2)) (rest nums) nums)))

(defn is-safe? [nums]
  (and (ordered? nums) (adjacent-diff? nums)))

(def ans (->> (slurp "in.txt")
              str/split-lines
              (map (fn [line] (map #(Integer/parseInt %) (str/split line #" "))))
              (map is-safe?)
              (filter true?)
              count))

(println ans)

(defn remove-each [nums]
  (map-indexed
   (fn [idx _]
     (concat (take idx nums) (drop (inc idx) nums)))
   nums))

(defn is-safe2? [nums]
  (some #(and (ordered? %) (adjacent-diff? %)) (remove-each nums)))

(def ans2 (->> (slurp "in.txt")
               str/split-lines
               (map (fn [line] (map #(Integer/parseInt %) (str/split line #" "))))
               (map is-safe2?)
               (filter true?)
               count))

(println ans2)