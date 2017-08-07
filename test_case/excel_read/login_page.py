
class LoginPage:
    def get_excel(self, excel_file):
            try:
                data = xlrd.open_workbook(excel_file)
                table = data.sheets()[0]
                return table
            except:
                return False

        def get_rows(self):
            table = self.get_excel('./test_case/excel_read/login_data.xlsx')
            if table:
                rows = table.nrows
                return rows
            else:
                print ('1. The excel file not exit !')

        def get_cols(self):
            table = self.get_excel('./test_case/excel_read/login_data.xlsx')
            if table:
                cols = table.ncols
                return cols
            else:
                print ('2. The excel not exit !')

        def get_login_dict(self):
            table = self.get_excel('./test_case/excel_read/login_data.xlsx')
            login_dict = {}
            rows = self.get_rows()
            cols = self.get_cols()

            for i in range(rows):
                for j in range(cols):
                    login_dict[table.cell(i, j).value] = table.cell(i, i).value
                return list(login_dict.items())