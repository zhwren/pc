#include "acp_type.h"
#include "acp_database.h"

int32 main()
{
    AcpDB* acpDb = new AcpDB("..\\..\\data\\db");
    if( acpDb==NULL )
    {
        return 0;
    }

    acpDb->GetRecord();

    delete acpDb;
}