(def x (list 1 2 3 4 5))

(defn cubic [param1]
    (* param1 param1 param1)
)

(println(map cubic x))