(require '[clojure.string :as str])

(def data (slurp "in.txt"))

(def lines (str/split-lines data))

(def lengths (map Integer/parseInt (str/split (first lines) #",")))

(def size 256)

(def nums (loop [lengths lengths
                 nums (vec (range size))
                 cur-pos 0
                 skip-size 0]
            (if (empty? lengths)
              nums
              (let [length (first lengths)
                    cur-nums (into (subvec nums cur-pos (min (+ cur-pos length) size))
                                   (subvec nums 0 (max (+ cur-pos length (- size)) 0)))
                    rev-nums (reverse cur-nums)
                    nums' (loop [i cur-pos nums' nums]
                            (if (>= i (+ cur-pos length))
                              nums'
                              (recur (inc i) (assoc nums' (mod i size) (nth rev-nums  (- i cur-pos))))))
                    cur-pos' (mod (+ cur-pos length skip-size) size)
                    skip-size' (inc skip-size)]
                (recur (rest lengths) nums' cur-pos' skip-size')))))

(println (* (first nums) (second nums)))