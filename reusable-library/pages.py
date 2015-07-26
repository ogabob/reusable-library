
class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
      <title>Enter Information:</title>
      <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = ""
        self.__error = ''
        self.__close = """
    <body>
</html>
                """
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all


class Page2(object):
    def __init__(self):
        self.sect1 = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Sell your Car</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
        """

        self.sect2 = """
    <body>
        <form method = "GET">
            <label>Make: <input type = "text" name="make" /> </label>
            <br />
            <br />
            <label>Model: <input type = "text" name="model" /> </label>
            <br />
            <br />
            <label>Year: <input type = "text" name="year" /> </label>
            <br />
            <br />
            <label>Body Style: <input type = "text" name="bds" /> </label>
            <br />
            <br />
            <label>Vin Number: <input type = "text" name="vin" /> </label>
            <br />
            <br />
            <label>How Many Miles: <input type = "text" name="miles" /> </label>
            <br />
            <br />


    </body>
                """
        self.sect3 = """
</html>
                """
    def print_out2(self):
        return self.sect1 + self.sect2 + self.sect3
