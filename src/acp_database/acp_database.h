
#ifndef ACP_DATABASE_H
#define ACP_DATABASE_H 1

#include <string>
#include "acp_type.h"
using namespace std;

struct sqlite3;
class CLASS_EXPORT AcpDB
{
public:
    AcpDB();
    AcpDB(string filename);
    ~AcpDB();

public:
    int32 GetRecord();

private:
    sqlite3* db;
};
#endif