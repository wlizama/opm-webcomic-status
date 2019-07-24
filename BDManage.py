import sqlite3

class BDManage:

    BD_NAME = "BD_OPM_WC.db"

    def __init__(self):
        self.__connection = None


    @property
    def connection(self):
        return self.__connection


    def connect(self):
        self.__connection = sqlite3.connect(self.BD_NAME)


    def disconnect(self):
        self.connection.close()


    def commit_trans(self):
        self.connection.commit()


    def __get_cursor(self):
        return self.connection.cursor()


    def execute_sttmt(self, sttmt):
        try:
            self.connect()
            self.__get_cursor().execute(sttmt)
        except Exception as ex:
            print('Exception Msg: "%s"' % ex)
            raise(ex)
        else:
            self.commit_trans()
        finally:
            self.disconnect()


    def execute_insert(self, sttmt, values=None):
        try:
            self.connect()
            self.__get_cursor().execute(sttmt, values)
        except Exception as ex:
            print('Exception Msg: "%s"' % ex)
            raise(ex)
        else:
            self.commit_trans()
        finally:
            self.disconnect()


    def execute_select_one(self, sttmt):
        result = None
        try:
            self.connect()
            result = self.__get_cursor().execute(sttmt).fetchone()
        except Exception as ex:
            print('Exception Msg: "%s"' % ex)
            raise(ex)
        finally:
            self.disconnect()

        return result


    def execute_select_all(self, sttmt):
        result = None
        try:
            self.connect()
            result = self.__get_cursor().execute(sttmt).fetchall()
        except Exception as ex:
            print('Exception Msg: "%s"' % ex)
            raise(ex)
        finally:
            self.disconnect()

        return result


    def execute_delete(self, sttmt):
        result = 0
        try:
            self.connect()
            result = self.__get_cursor().execute(sttmt).rowcount
        except Exception as ex:
            print('Exception Msg: "%s"' % ex)
            raise(ex)
        else:
            self.commit_trans()
        finally:
            self.disconnect()

        return result


# if __name__ == "__main__":
#     c = BDManage()
#     c.init_tables()
#     c.add_capitulo(160, 'OPM Inicio 2', 'Lorem asd asww mod')
#     c.add_capitulo(161, 'OPM Inicio 3', 'Lorem asd asww mod')
#     c.add_capitulo(162, 'OPM Inicio 4', 'Lorem asd asww mod')
#     c.add_capitulo(163, 'OPM Inicio 5', 'Lorem asd asww mod')
#     # print(c.execute_select_all("select * from capitulo"))
#     # print(c.execute_delete("delete from capitulo"))
#     # print(c.get_records())