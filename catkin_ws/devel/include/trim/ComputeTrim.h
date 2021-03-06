// Generated by gencpp from file trim/ComputeTrim.msg
// DO NOT EDIT!


#ifndef TRIM_MESSAGE_COMPUTETRIM_H
#define TRIM_MESSAGE_COMPUTETRIM_H

#include <ros/service_traits.h>


#include <trim/ComputeTrimRequest.h>
#include <trim/ComputeTrimResponse.h>


namespace trim
{

struct ComputeTrim
{

typedef ComputeTrimRequest Request;
typedef ComputeTrimResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ComputeTrim
} // namespace trim


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::trim::ComputeTrim > {
  static const char* value()
  {
    return "7777883b607700a320089ca7a9d2af0e";
  }

  static const char* value(const ::trim::ComputeTrim&) { return value(); }
};

template<>
struct DataType< ::trim::ComputeTrim > {
  static const char* value()
  {
    return "trim/ComputeTrim";
  }

  static const char* value(const ::trim::ComputeTrim&) { return value(); }
};


// service_traits::MD5Sum< ::trim::ComputeTrimRequest> should match 
// service_traits::MD5Sum< ::trim::ComputeTrim > 
template<>
struct MD5Sum< ::trim::ComputeTrimRequest>
{
  static const char* value()
  {
    return MD5Sum< ::trim::ComputeTrim >::value();
  }
  static const char* value(const ::trim::ComputeTrimRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::trim::ComputeTrimRequest> should match 
// service_traits::DataType< ::trim::ComputeTrim > 
template<>
struct DataType< ::trim::ComputeTrimRequest>
{
  static const char* value()
  {
    return DataType< ::trim::ComputeTrim >::value();
  }
  static const char* value(const ::trim::ComputeTrimRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::trim::ComputeTrimResponse> should match 
// service_traits::MD5Sum< ::trim::ComputeTrim > 
template<>
struct MD5Sum< ::trim::ComputeTrimResponse>
{
  static const char* value()
  {
    return MD5Sum< ::trim::ComputeTrim >::value();
  }
  static const char* value(const ::trim::ComputeTrimResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::trim::ComputeTrimResponse> should match 
// service_traits::DataType< ::trim::ComputeTrim > 
template<>
struct DataType< ::trim::ComputeTrimResponse>
{
  static const char* value()
  {
    return DataType< ::trim::ComputeTrim >::value();
  }
  static const char* value(const ::trim::ComputeTrimResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TRIM_MESSAGE_COMPUTETRIM_H
