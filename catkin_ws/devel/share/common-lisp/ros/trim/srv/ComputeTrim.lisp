; Auto-generated. Do not edit!


(cl:in-package trim-srv)


;//! \htmlinclude ComputeTrim-request.msg.html

(cl:defclass <ComputeTrim-request> (roslisp-msg-protocol:ros-message)
  ((Va
    :reader Va
    :initarg :Va
    :type cl:float
    :initform 0.0)
   (gamma
    :reader gamma
    :initarg :gamma
    :type cl:float
    :initform 0.0)
   (R
    :reader R
    :initarg :R
    :type cl:float
    :initform 0.0))
)

(cl:defclass ComputeTrim-request (<ComputeTrim-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ComputeTrim-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ComputeTrim-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trim-srv:<ComputeTrim-request> is deprecated: use trim-srv:ComputeTrim-request instead.")))

(cl:ensure-generic-function 'Va-val :lambda-list '(m))
(cl:defmethod Va-val ((m <ComputeTrim-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trim-srv:Va-val is deprecated.  Use trim-srv:Va instead.")
  (Va m))

(cl:ensure-generic-function 'gamma-val :lambda-list '(m))
(cl:defmethod gamma-val ((m <ComputeTrim-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trim-srv:gamma-val is deprecated.  Use trim-srv:gamma instead.")
  (gamma m))

(cl:ensure-generic-function 'R-val :lambda-list '(m))
(cl:defmethod R-val ((m <ComputeTrim-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trim-srv:R-val is deprecated.  Use trim-srv:R instead.")
  (R m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ComputeTrim-request>) ostream)
  "Serializes a message object of type '<ComputeTrim-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Va))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'gamma))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'R))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ComputeTrim-request>) istream)
  "Deserializes a message object of type '<ComputeTrim-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Va) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gamma) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'R) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ComputeTrim-request>)))
  "Returns string type for a service object of type '<ComputeTrim-request>"
  "trim/ComputeTrimRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ComputeTrim-request)))
  "Returns string type for a service object of type 'ComputeTrim-request"
  "trim/ComputeTrimRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ComputeTrim-request>)))
  "Returns md5sum for a message object of type '<ComputeTrim-request>"
  "d00a817e9be7d657a0cb7e630d53cf0e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ComputeTrim-request)))
  "Returns md5sum for a message object of type 'ComputeTrim-request"
  "d00a817e9be7d657a0cb7e630d53cf0e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ComputeTrim-request>)))
  "Returns full string definition for message of type '<ComputeTrim-request>"
  (cl:format cl:nil "float64 Va~%float64 gamma~%float64 R~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ComputeTrim-request)))
  "Returns full string definition for message of type 'ComputeTrim-request"
  (cl:format cl:nil "float64 Va~%float64 gamma~%float64 R~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ComputeTrim-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ComputeTrim-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ComputeTrim-request
    (cl:cons ':Va (Va msg))
    (cl:cons ':gamma (gamma msg))
    (cl:cons ':R (R msg))
))
;//! \htmlinclude ComputeTrim-response.msg.html

(cl:defclass <ComputeTrim-response> (roslisp-msg-protocol:ros-message)
  ((x_trim
    :reader x_trim
    :initarg :x_trim
    :type (cl:vector cl:float)
   :initform (cl:make-array 12 :element-type 'cl:float :initial-element 0.0))
   (u_trim
    :reader u_trim
    :initarg :u_trim
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass ComputeTrim-response (<ComputeTrim-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ComputeTrim-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ComputeTrim-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trim-srv:<ComputeTrim-response> is deprecated: use trim-srv:ComputeTrim-response instead.")))

(cl:ensure-generic-function 'x_trim-val :lambda-list '(m))
(cl:defmethod x_trim-val ((m <ComputeTrim-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trim-srv:x_trim-val is deprecated.  Use trim-srv:x_trim instead.")
  (x_trim m))

(cl:ensure-generic-function 'u_trim-val :lambda-list '(m))
(cl:defmethod u_trim-val ((m <ComputeTrim-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trim-srv:u_trim-val is deprecated.  Use trim-srv:u_trim instead.")
  (u_trim m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ComputeTrim-response>) ostream)
  "Serializes a message object of type '<ComputeTrim-response>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'x_trim))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'u_trim))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ComputeTrim-response>) istream)
  "Deserializes a message object of type '<ComputeTrim-response>"
  (cl:setf (cl:slot-value msg 'x_trim) (cl:make-array 12))
  (cl:let ((vals (cl:slot-value msg 'x_trim)))
    (cl:dotimes (i 12)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  (cl:setf (cl:slot-value msg 'u_trim) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'u_trim)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ComputeTrim-response>)))
  "Returns string type for a service object of type '<ComputeTrim-response>"
  "trim/ComputeTrimResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ComputeTrim-response)))
  "Returns string type for a service object of type 'ComputeTrim-response"
  "trim/ComputeTrimResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ComputeTrim-response>)))
  "Returns md5sum for a message object of type '<ComputeTrim-response>"
  "d00a817e9be7d657a0cb7e630d53cf0e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ComputeTrim-response)))
  "Returns md5sum for a message object of type 'ComputeTrim-response"
  "d00a817e9be7d657a0cb7e630d53cf0e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ComputeTrim-response>)))
  "Returns full string definition for message of type '<ComputeTrim-response>"
  (cl:format cl:nil "float64[12] x_trim~%float64[4] u_trim~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ComputeTrim-response)))
  "Returns full string definition for message of type 'ComputeTrim-response"
  (cl:format cl:nil "float64[12] x_trim~%float64[4] u_trim~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ComputeTrim-response>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'x_trim) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'u_trim) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ComputeTrim-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ComputeTrim-response
    (cl:cons ':x_trim (x_trim msg))
    (cl:cons ':u_trim (u_trim msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ComputeTrim)))
  'ComputeTrim-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ComputeTrim)))
  'ComputeTrim-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ComputeTrim)))
  "Returns string type for a service object of type '<ComputeTrim>"
  "trim/ComputeTrim")