(require '[clojure.string :as str])

(def data (slurp "in.txt"))

(def chunks (str/split data #"\n\n"))

(def orders (str/split  (first chunks) #"\n"))

(def followers (loop [orders orders
                      followers {}]
                 (if (empty? orders)
                   followers
                   (let [[followed follower]
                         (mapv Integer/parseInt (str/split (first orders) #"\|"))]
                     (recur (rest orders)
                            (update followers followed (fnil conj []) follower))))))

(def updates (->> (str/split (second chunks) #"\n")
                  (mapv #(mapv Integer/parseInt (str/split % #",")))))

(defn ordered? [nums] (loop [nums nums
                             seen #{}]
                        (if (empty? nums)
                          true
                          (let [num (first nums)
                                follows (get followers num [])]
                            (if (some seen follows)
                              false
                              (recur (rest nums) (conj seen num)))))))

(defn swap-nums [num follow nums seen]
  (let [num_at (seen num)
        follow_at (seen follow)]
    [(-> nums
         (assoc num_at (nth nums follow_at))
         (assoc follow_at (nth nums num_at)))
     (-> seen
         (assoc follow num_at)
         (assoc num follow_at))]))

(defn order-num [num follows nums seen]
  (reduce
   (fn [[nums seen] follow]
     (if (and (contains? seen follow)
              (< (seen follow) (seen num)))
       (swap-nums num follow nums seen)
       [nums seen]))
   [nums seen]
   follows))

(defn order-at-idx [idx nums seen]
  (let [num (nth nums idx)
        follows (get followers num [])
        seen (assoc seen num idx)
        [nums seen] (order-num num follows nums seen)]
    [nums seen]))

(defn order-nums [nums]
  (if (ordered? nums)
    nums
    (let [[nums _]
          (reduce
           (fn [[nums seen] i] (order-at-idx i nums seen))
           [nums {}]
           (range (count nums)))]
      (order-nums nums))))

(def ans (->> updates
              (mapv (fn [nums]
                      (if (ordered? nums)
                        (nth nums (quot (count nums) 2))
                        0)))
              (reduce +)))

(def ans2 (->> updates
               (mapv  (fn [nums]
                        (if (not (ordered? nums))
                          (nth (order-nums nums) (quot (count nums) 2))
                          0)))
               (reduce +)))

(println ans)
(println ans2)