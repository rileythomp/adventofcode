(require '[clojure.string :as str])

(let [pairs (->> (slurp "in.txt")
                 str/split-lines
                 (map #(str/split % #"   ")))
      lefts (sort (map #(Integer/parseInt (first %)) pairs))
      rights (sort (map #(Integer/parseInt (second %)) pairs))
      ans (->> (map #(abs (- %1 %2)) lefts rights)
               (reduce +))]
  (println ans))

(let [pairs (->> (slurp "in.txt")
                 str/split-lines
                 (map #(str/split % #"   ")))
      lefts (sort (map #(Integer/parseInt (first %)) pairs))
      rights (sort (map #(Integer/parseInt (second %)) pairs))
      ans (->> (map #(* % ((frequencies rights) % 0)) lefts)
               (reduce +))]
  (println ans))

