(defun sum(a b c)
  (+ a b c)
)
(print (sum 1 2 3))

(defun quad(a)
  (print(* a a))
)
(defparameter x 4)
(quad x)

(defparameter myList (list 1 2 3))
(print (car myList))
(print (cdr myList))
(print (cons 1 myList))
(print (append myList (list 4 5)))
(print (last myList))
(print (member 4 myList))
(print (reverse myList))

(loop for x in myList
      do (print x))

(loop repeat 3
      do (print "p"))

(if (> 4 5)
    (print "4 é > 5")
    (print "4 é < 5")
)

(defun triple(x)
  (if(> x 1)
    (* x 3)
    (* x 8)
  )
)
(print (mapcar #'triple myList))
(print (mapcar #'(lambda (arg) (* arg 4)) myList))