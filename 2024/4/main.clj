(require '[clojure.string :as str])

(def data (slurp "in.txt"))

(def lines (str/split-lines data))

(def grid (mapv #(vec %) lines))

(def xmas '(\X \M \A \S))
(def ms '(\M \S))

(defn xmas-match? [word]
  (if (contains? #{xmas (reverse xmas)} word) 1 0))

(defn count-xmas [y x]
  (+ (xmas-match? (map #(get-in grid [y (+ x %)]) (range 4)))
     (xmas-match? (map #(get-in grid [(+ y %) x]) (range 4)))
     (xmas-match? (map #(get-in grid [(+ y %) (+ x %)]) (range 4)))
     (xmas-match? (map #(get-in grid [(+ y %) (- x %)]) (range 4)))))

(def xmas-counts (mapv (fn [row y] (mapv (fn [_ x] (count-xmas y x)) row (range))) grid (range)))

(defn xmas-match2? [corner1 corner2]
  (contains? #{ms (reverse ms)} (list (get-in grid corner1) (get-in grid corner2))))

(defn count-xmas2 [y x]
  (if (and (= ((grid y) x) \A)
           (xmas-match2? [(- y 1) (- x 1)] [(+ y 1) (+ x 1)])
           (xmas-match2? [(- y 1) (+ x 1)] [(+ y 1) (- x 1)])) 1 0))

(def xmas-counts-2 (mapv (fn [row y] (mapv (fn [_ x] (count-xmas2 y x)) row (range))) grid (range)))

(def ans (reduce + (mapv #(reduce + %) xmas-counts)))
(def ans2 (reduce + (mapv #(reduce + %) xmas-counts-2)))

(println ans)
(println ans2)
