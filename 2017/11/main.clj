(require '[clojure.string :as str])

(def data (slurp "in.txt"))

(def lines (str/split-lines data))

(def moves (str/split (first lines) #","))

(def dirs {"n" [1 -1 0]
           "s" [-1 1 0]
           "ne" [1 0 -1]
           "sw" [-1 0 1]
           "nw" [0 -1 1]
           "se" [0 1 -1]})

(defn hex-dist [coords] (apply max (map Math/abs coords)))

(def ans
  (loop [moves moves
         coords [0 0 0]
         max-dist 0]
    (if (empty? moves)
      [(hex-dist coords) max-dist]
      (let [move (first moves)
            coords' (mapv + coords (dirs move))
            max-dist' (max max-dist (hex-dist coords'))]
        (recur (rest moves) coords' max-dist')))))

(println (first ans))
(println (second ans))