(def data (slurp "in.txt"))

(def mult-pattern #"mul\((\d+),(\d+)\)")
(def do-pattern #"do\(\)")
(def dont-pattern #"don't\(\)")

(defn get-idxs [pattern data]
  (let [matcher (re-matcher pattern data)]
    (loop [idxs []]
      (if (.find matcher)
        (recur (conj idxs (.start matcher)))
        idxs))))

(def do-idxs (get-idxs do-pattern data))
(def dont-idxs (get-idxs dont-pattern data))

(defn mult-instruction [[idx n1 n2]]
  (let [do-idx (last (cons 0 (filter #(< % idx) do-idxs)))
        dont-idx (last (cons 0 (filter #(< % idx) dont-idxs)))]
    (if (>= do-idx dont-idx)
      (* n1 n2)
      0)))

(def ans (->> data
              (re-seq mult-pattern)
              (map #(* (Integer/parseInt (nth % 1)) (Integer/parseInt (nth % 2))))
              (reduce +)))

(def mults (re-matcher mult-pattern data))
(def mult-idxs (loop [idxs []]
                 (if (.find mults)
                   (recur (conj idxs (list (.start mults)
                                           (Integer/parseInt (.group mults 1))
                                           (Integer/parseInt (.group mults 2)))))
                   idxs)))

(def ans2 (->> mult-idxs
               (map mult-instruction)
               (reduce +)))

(println ans)
(println ans2)
