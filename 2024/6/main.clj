(require '[clojure.string :as str])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(def grid (mapv vec lines))

(def init-coord (some (fn [[y row]]
                        (when-let [x (some (fn [[x cell]]
                                             (when (= \^ cell) x))
                                           (map-indexed  vector row))]
                          [y x]))
                      (map-indexed vector grid)))

(defn turn [cury curx move]
  (case move
    0 [(inc cury) curx (mod (inc move) 4)]
    1 [cury (dec curx) (mod (inc move) 4)]
    2 [(dec cury) curx (mod (inc move) 4)]
    3 [cury (inc curx) (mod (inc move) 4)]))

(defn advance [cury curx move]
  (case move
    0 [(dec cury) curx move]
    1 [cury (inc curx) move]
    2 [(inc cury) curx move]
    3 [cury (dec curx) move]))

(def visited (loop [cury (first init-coord)
                    curx (second init-coord)
                    move 0
                    visited #{}]
               (if (and (>= cury 0)
                        (< cury (count grid))
                        (>= curx 0)
                        (< curx  (count (first grid))))
                 (let [[cury curx move] (if (= (get-in grid [cury curx]) \#)
                                          (turn cury curx move)
                                          [cury curx move])
                       seen' (conj visited [cury curx])
                       [cury' curx' move'] (advance cury curx move)]
                   (recur cury' curx' move' seen'))
                 visited)))

(def ans (count visited))

(def ans2 (->> visited
               (map
                (fn [[blocky blockx]]
                  (loop [ans2 0
                         grid (assoc-in grid [blocky blockx] \#)
                         cury (first init-coord)
                         curx (second init-coord)
                         move 0
                         visited #{}]
                    (if (and (>= cury 0)
                             (< cury (count grid))
                             (>= curx 0)
                             (< curx  (count (first grid)))
                             (= 0 ans2))
                      (let [ans2' (if (contains? visited [cury curx move]) 1 0)
                            [cury curx move] (if (= (get-in grid [cury curx]) \#)
                                               (turn cury curx move)
                                               [cury curx move])
                            seen' (conj visited [cury curx move])
                            [cury' curx' move'] (advance cury curx move)]
                        (recur ans2' grid cury' curx' move' seen'))
                      ans2))))
               (reduce +)))

(println ans)
(println ans2)