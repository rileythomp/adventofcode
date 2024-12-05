(require '[clojure.string :as str])

(def data (slurp "in.txt"))

(def chunks (str/split data #"\n\n"))

(def orders (str/split  (first chunks) #"\n"))

(def followers (loop [orders orders
                      followers {}]
                 (if (empty? orders) followers
                   (let [[followed follower]
                         (mapv Integer/parseInt (str/split (first orders) #"\|"))]
                     (recur (rest orders)
                            (update followers followed (fnil conj []) follower))))))

(def updates (->> (str/split (second chunks) #"\n") 
                  (mapv #(mapv Integer/parseInt (str/split % #",")))))

(defn ordered? [nums] (loop [nums nums seen {}]
                        (if (empty? nums) true
                          (let [num (first nums)
                                follows (get followers num [])]
                            (if (some #(contains? seen %) follows) false
                              (recur (rest nums) (assoc seen num true)))))))

(defn reorder [nums]
  (if (ordered? nums) nums
    (reorder (loop [i 0 nums nums seen {}]
               (if (>= i (count nums)) nums
                   (let [num (nth nums i)
                         follows (get followers num [])
                         seen (assoc seen num i)
                         numseen (loop [follows follows seen seen nums nums]
                                   (if (empty? follows)
                                     [nums seen]
                                     (let [follow (first follows)]
                                       (if (and (contains? seen follow) (< (seen follow) (seen num)))
                                         (let [num_at (seen num)
                                               follow_at (seen follow)
                                               nums_follow_at (nth nums follow_at)
                                               nums_num_at (nth nums num_at)
                                               nums' (-> nums
                                                         (assoc num_at nums_follow_at)
                                                         (assoc follow_at nums_num_at))
             
                                               seen' (-> seen
                                                         (assoc follow num_at)
                                                         (assoc num follow_at))]
                                           (recur (rest follows) seen' nums'))
                                         (recur (rest follows) seen nums)))))]
                     (recur (inc i) (first numseen) (second numseen))))))))
  
(def ans (->> updates
              (mapv (fn [nums] 
                      (if (ordered? nums)
                        (nth nums (quot (count nums) 2))
                        0)))
              (reduce +)))

(def ans2 (->> updates
               (mapv  (fn [nums]
                        (if (not (ordered? nums))
                          (nth (reorder nums) (quot (count nums) 2))
                          0)))
               (reduce +)))

(println ans)
(println ans2)