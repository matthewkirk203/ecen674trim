
(cl:in-package :asdf)

(defsystem "trim-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ComputeTrim" :depends-on ("_package_ComputeTrim"))
    (:file "_package_ComputeTrim" :depends-on ("_package"))
  ))