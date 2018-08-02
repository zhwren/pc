#include "sqlite3.h"
#include "acp_database.h"

AcpDB::AcpDB(string filename)
{
    int rc = sqlite3_open(filename.c_str(), &db);
    if( rc!=0 )
    {
        ;
    }
}

AcpDB::AcpDB()
{
    sqlite3_close(db);
}

AcpDB::~AcpDB()
{

}

static int32 test(void* data, int argc, char** argv, char** colName)
{
    for(int32 i=0; i<argc; i++)
    {
        printf("%s:%s ", colName[i], argv[i]);
    }
    printf("\n");
    return 0;
}
int32 AcpDB::GetRecord()
{
    char* errMsg;
    string sql = "select CONTENT from DB_PEOTYS where TITLE='ÐÐ¹¬'";
    int32 rc = sqlite3_exec(db, sql.c_str(), test, 0, &errMsg);
    return rc;
}