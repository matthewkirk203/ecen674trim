// Generated by gencpp from file trim/ComputeTrimRequest.msg
// DO NOT EDIT!


#ifndef TRIM_MESSAGE_COMPUTETRIMREQUEST_H
#define TRIM_MESSAGE_COMPUTETRIMREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace trim
{
template <class ContainerAllocator>
struct ComputeTrimRequest_
{
  typedef ComputeTrimRequest_<ContainerAllocator> Type;

  ComputeTrimRequest_()
    : Va(0.0)
    , gamma(0.0)
    , R(0.0)  {
    }
  ComputeTrimRequest_(const ContainerAllocator& _alloc)
    : Va(0.0)
    , gamma(0.0)
    , R(0.0)  {
    }



   typedef double _Va_type;
  _Va_type Va;

   typedef double _gamma_type;
  _gamma_type gamma;

   typedef double _R_type;
  _R_type R;




  typedef boost::shared_ptr< ::trim::ComputeTrimRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::trim::ComputeTrimRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ComputeTrimRequest_

typedef ::trim::ComputeTrimRequest_<std::allocator<void> > ComputeTrimRequest;

typedef boost::shared_ptr< ::trim::ComputeTrimRequest > ComputeTrimRequestPtr;
typedef boost::shared_ptr< ::trim::ComputeTrimRequest const> ComputeTrimRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::trim::ComputeTrimRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::trim::ComputeTrimRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace trim

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::trim::ComputeTrimRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::trim::ComputeTrimRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::trim::ComputeTrimRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::trim::ComputeTrimRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::trim::ComputeTrimRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::trim::ComputeTrimRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::trim::ComputeTrimRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "808d6dad1d12679a9e05848ee2a620e6";
  }

  static const char* value(const ::trim::ComputeTrimRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x808d6dad1d12679aULL;
  static const uint64_t static_value2 = 0x9e05848ee2a620e6ULL;
};

template<class ContainerAllocator>
struct DataType< ::trim::ComputeTrimRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "trim/ComputeTrimRequest";
  }

  static const char* value(const ::trim::ComputeTrimRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::trim::ComputeTrimRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 Va\n\
float64 gamma\n\
float64 R\n\
";
  }

  static const char* value(const ::trim::ComputeTrimRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::trim::ComputeTrimRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Va);
      stream.next(m.gamma);
      stream.next(m.R);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ComputeTrimRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::trim::ComputeTrimRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::trim::ComputeTrimRequest_<ContainerAllocator>& v)
  {
    s << indent << "Va: ";
    Printer<double>::stream(s, indent + "  ", v.Va);
    s << indent << "gamma: ";
    Printer<double>::stream(s, indent + "  ", v.gamma);
    s << indent << "R: ";
    Printer<double>::stream(s, indent + "  ", v.R);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TRIM_MESSAGE_COMPUTETRIMREQUEST_H
