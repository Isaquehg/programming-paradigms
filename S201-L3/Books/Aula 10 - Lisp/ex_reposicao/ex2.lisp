;;; Variáveis
(defparameter myList1 (list 1 2 3))
(defparameter myList2 (list 4 5 6))

;;; Função
(defun func1(a)
    (if (>= a 4)
        (* a a)
        (/ a 2)
    )
)

;;; Iteração, merge & output
(print (append (mapcar #'func1 myList1) (mapcar #'func1 myList2)))