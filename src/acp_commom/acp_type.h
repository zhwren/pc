
#ifndef ACP_TYPE_H
#define ACP_TYPE_H 1

#ifndef __GNUC__
#define CLASS_EXPORT __declspec(dllexport)
#else
#define CLASS_EXPORT
#endif

typedef char           int8;
typedef short          int16;
typedef int            int32;
typedef long           int64;

typedef unsigned char  uint8;
typedef unsigned short uint16;
typedef unsigned int   uint32;
typedef unsigned long  uint64;

#endif