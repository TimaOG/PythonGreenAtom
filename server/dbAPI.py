from db.dbWork import inbox
from databases import Database
from db.dbWork import database

class BaseRep:
    def __init__(self, database: Database):
        self.database = database

class InboxRep(BaseRep):

    async def getByCode(self, code: int):
        query = inbox.select().where(inbox.c.Code == code)
        inboxs = await self.database.fetch_all(query=query)
        return inboxs

    async def createImg(self, code: int, name: str, dateAndTime: str):
        query = inbox.insert().values(Code=code, fileName=name, DateAndTime=dateAndTime)
        await self.database.execute(query)


    async def delImg(self, code: int):
        query = inbox.delete().where(inbox.c.Code == code)
        await self.database.execute(query)

