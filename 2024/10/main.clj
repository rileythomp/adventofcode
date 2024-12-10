(require '[clojure.string :as str])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(def grid (mapv (fn [line] (mapv #(Character/digit % 10) line)) lines))

(defn in-bounds? [grid y x]
  (and (<= 0 y (dec (count grid)))
       (<= 0 x (dec (count (first grid))))))

(defn count-trails [grid y x]
  (loop [queue [[(get-in grid [y x]) [y x]]]
         seen #{}
         trails 0
         trails2 0]
    (if (empty? queue)
      [trails trails2]
      (let [[val [y x]] (first queue)]
        (cond (and (= val 9) (not (contains? seen [y x])))
              (recur (rest queue) (conj seen [y x]) (inc trails) (inc trails2))
              (= val 9)
              (recur (rest queue) seen trails (inc trails2))
              :else
              (let [queue' (->> [[y, (dec x)] [y, (inc x)] [(dec y), x] [(inc y), x]]
                                (filter (fn [[y x]] (and (in-bounds? grid y x)
                                                         (= (inc val) (get-in grid [y x])))))
                                (map (fn [nbr] [(inc val) nbr]))
                                (concat (rest queue)))]
                (recur queue' seen trails trails2)))))))

(def trails (reduce
             (fn [[ans ans2] [y row]]
               (reduce
                (fn [[ans ans2] [x cell]]
                  (if (zero? cell)
                    (let [[trails trails2] (count-trails grid y x)]
                      [(+ ans trails) (+ ans2 trails2)])
                    [ans ans2]))
                [ans ans2]
                (map-indexed vector row)))
             [0 0]
             (map-indexed vector grid)))

(println (first trails))
(println (second trails))