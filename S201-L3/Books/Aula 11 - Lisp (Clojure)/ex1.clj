;; Create list variable
(def x (list 1 2 3 4 5))
(def y (list 6 7 8 9 10))

;; Create Function
(defn cubic [param1]
    (* param1 param1 param1)
)

;; Concatenate and reverse two lists
(println (reverse (conj x y)))

;; Map a function
(println(map cubic x))