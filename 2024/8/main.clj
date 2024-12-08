(require '[clojure.string :as str])
(require '[clojure.math.combinatorics :as combo])

(def data (slurp (first *command-line-args*)))

(def lines (str/split data #"\n"))

(def grid (mapv (fn [line] (into [] line)) lines))

(def freqs (reduce (fn [freqs [y row]]
                     (reduce (fn [freqs [x cell]]
                               (if (not= cell \.)
                                 (update freqs cell (fnil conj []) [y x])
                                 freqs))
                             freqs
                             (map-indexed vector row)))
                   {}
                   (map-indexed vector grid)))

(defn in-bounds? [[y x]]
  (and (>= y 0) (< y (count grid))
       (>= x 0) (< x (count (grid 0)))))

(defn add-obstacles [seen [p1 p2]]
  (cond-> seen
    (in-bounds? p1) (conj p1)
    (in-bounds? p2) (conj p2)))

(defn get-obstacles [[y1 x1] [y2 x2] dy dx]
  [[(- y1 dy) (- x1 dx)] [(+ y2 dy) (+ x2 dx)]])

(def ans (->> freqs
              (reduce-kv (fn [seen _ coords]
                           (reduce (fn [seen [[y1 x1 :as p1] [y2 x2 :as p2]]]
                                     (add-obstacles seen
                                                    (get-obstacles p1 p2 (- y2 y1) (- x2 x1))))
                                   seen
                                   (combo/combinations coords 2)))
                         #{})
              count))

(def ans2 (->> freqs
               (reduce-kv (fn [seen _ coords]
                            (reduce (fn [seen [[y1 x1 :as p1] [y2 x2 :as p2]]]
                                      (let [dy (- y2 y1) dx (- x2 x1)]
                                        (loop [seen (conj seen p1 p2)
                                               [p1 p2] (get-obstacles p1 p2 dy dx)]
                                          (if (or (in-bounds? p1)
                                                  (in-bounds? p2))
                                            (recur (add-obstacles seen [p1 p2])
                                                   (get-obstacles p1 p2 dy dx))
                                            seen))))
                                    seen
                                    (combo/combinations coords 2)))
                          #{})
               count))

(println ans)
(println ans2)