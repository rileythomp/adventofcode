(require '[clojure.string :as str])

(def pairs (->> (slurp "in.txt")
                str/split-lines
                (map #(str/split % #"   "))))

(def lefts (sort (map #(Integer/parseInt (first %)) pairs)))
(def rights (sort (map #(Integer/parseInt (second %)) pairs)))

(println (reduce + (map #(abs (- %1 %2)) lefts rights)))
(println (reduce + (map #(* % ((frequencies rights) % 0)) lefts)))