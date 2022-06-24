from concurrent.futures import thread
from sqlite3 import Row
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    executable_path=r"/Users/gaberogers/Desktop/3_in_a_row/chromedriver")

class Board:
    def __init__(self):
        self.board = []
        self.size = 0

    def makeBoard(self, size):
        driver.get('https://brainbashers.com/3inarow.asp')
        if size == 18:
            special = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[2]/blockquote/p[2]/a[11]')))
            special.click()
        else:
            date = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="date"]')))
            date.click()
            random = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="date"]/option[12]')))
            random.click()
            selectSize = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]')))
            selectSize.click()
            sizeSelect = ((size - 6) / 2) + 1
            four10 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[' + str(sizeSelect) + ']')))
            four10.click()
            go = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[1]/form/blockquote/nobr/input[1]')))
            go.click()
        newBoard = []
        count = 0
        for j in range(0, size):
            row = []
            for i in range(count, size + count):
                square = driver.find_element(
                    By.XPATH, '//*[@id="square' + str(i) + '"]').get_attribute('class')[-1]
                row.append(square)
                count += 1
            newBoard.append(row)
        self.board = newBoard
        self.size = size

    def solveBoard(self):
        if self.board == "":
            return
        else:
            solvedRows = set()
            # while board not solved
            while len(solvedRows) < self.size:
                for a, r in enumerate(self.board):
                    blueCountCol = 0
                    whiteCountCol = 0
                    #solving columns
                    for i, c in enumerate(r):
                        if self.board[i][a] == "e":
                            whiteCountCol += 1
                        elif self.board[i][a] == "k":
                            blueCountCol += 1
                        else:
                            # if the square is two in from the top and bottom of the column
                            if (len(r)-2) > i > 1:
                                onePrev = self.board[i-1][a]
                                twoPrev = self.board[i-2][a]
                                nextOne = self.board[i+1][a]
                                nextTwo = self.board[i+2][a]
                                # if prev 2 are blue set c to white
                                if onePrev == "k" and twoPrev == "k":
                                    self.board[i][a] = "e"
                                # if prev 2 are white set c to blue
                                elif onePrev == "e" and twoPrev == "e":
                                    self.board[i][a] = "k"
                                # if next 2 are blue set c to white
                                elif nextOne == "k" and nextTwo == "k":
                                    self.board[i][a] = "e"
                                # if next two are white set c to blue
                                elif nextOne == "e" and nextTwo == "e":
                                    self.board[i][a] = "k"
                                # if one before and one after are blue set c to white
                                elif onePrev == "k" and nextOne == "k":
                                    self.board[i][a] = "e"
                                # if one before and one after are white set c to blue
                                elif onePrev == "e" and nextOne == "e":
                                    self.board[i][a] = "k"
                            elif (len(r)-1) > i > 0:
                                onePrev = self.board[i-1][a]
                                nextOne = self.board[i+1][a]
                                # if one before and one after are blue set c to white
                                if onePrev == "k" and nextOne == "k":
                                    self.board[i][a] = "e"
                                # if one before and one after are white set c to blue
                                elif onePrev == "e" and nextOne == "e":
                                    self.board[i][a] = "k"
                            if i > 2:
                                onePrev = self.board[i-1][a]
                                twoPrev = self.board[i-2][a]
                                if onePrev == "k" and twoPrev == "k":
                                    self.board[i][a] = "e"
                                # if prev 2 are white set c to blue
                                elif onePrev == "e" and twoPrev == "e":
                                    self.board[i][a] = "k"
                            if i < (len(r)-2):
                                nextOne = self.board[i+1][a]
                                nextTwo = self.board[i+2][a]
                                # if next 2 are blue set c to white
                                if nextOne == "k" and nextTwo == "k":
                                    self.board[i][a] = "e"
                                # if next two are white set c to blue
                                elif nextOne == "e" and nextTwo == "e":
                                    self.board[i][a] = "k"

                    # solving rows
                    blueCountRow = 0
                    whiteCountRow = 0
                    for i, c in enumerate(r):
                        if c == "k":
                            blueCountRow+=1
                        elif c == "e":
                            whiteCountRow+=1
                        else:
                            # if we are two square in from either end
                            if (len(r)-2) > i > 1:
                                # find the two prev and two post values
                                onePrev = self.board[a][i-1]
                                twoPrev = self.board[a][i-2]
                                nextOne = self.board[a][i+1]
                                nextTwo = self.board[a][i+2]
                                # if prev 2 are blue set c to white
                                if onePrev == "k" and twoPrev == "k":
                                    self.board[a][i] = "e"
                                # if prev 2 are white set c to blue
                                elif onePrev == "e" and twoPrev == "e":
                                    self.board[a][i] = "k"
                                # if next 2 are blue set c to white
                                elif nextOne == "k" and nextTwo == "k":
                                    self.board[a][i] = "e"
                                # if next two are white set c to blue
                                elif nextOne == "e" and nextTwo == "e":
                                    self.board[a][i] = "k"
                                # if one before and one after are blue set c to white
                                elif onePrev == "k" and nextOne == "k":
                                    self.board[a][i] = "e"
                                # if one before and one after are white set c to blue
                                elif onePrev == "e" and nextOne == "e":
                                    self.board[a][i] = "k"
                            # if we are 1 in from either end
                            elif (len(r)-1) > i > 0:
                                onePrev = self.board[a][i-1]
                                nextOne = self.board[a][i+1]
                                # if one before and one after are blue set c to white
                                if onePrev == "k" and nextOne == "k":
                                    self.board[a][i] = "e"
                                # if one before and one after are white set c to blue
                                elif onePrev == "e" and nextOne == "e":
                                    self.board[a][i] = "k"
                            if i > 2:
                                onePrev = self.board[a][i-1]
                                twoPrev = self.board[a][i-2]
                                # if prev 2 are blue set c to white
                                if onePrev == "k" and twoPrev == "k":
                                    self.board[a][i] = "e"
                                # if prev 2 are white set c to blue
                                elif onePrev == "e" and twoPrev == "e":
                                    self.board[a][i] = "k"
                            if i < (len(r)-2):
                                nextOne = self.board[a][i+1]
                                nextTwo = self.board[a][i+2]
                                # if next 2 are blue set c to white
                                if nextOne == "k" and nextTwo == "k":
                                    self.board[a][i] = "e"
                                # if next two are white set c to blue
                                elif nextOne == "e" and nextTwo == "e":
                                    self.board[a][i] = "k"

                    #Check if rows have 1 color finished, if they do complete them               
                    #if we have all the blues in the row make the remaining squares white
                    if blueCountRow == self.size / 2 and whiteCountRow != self.size / 2:
                        for i in range(self.size):
                            if self.board[a][i] == "y":
                                self.board[a][i] = "e"
                    #if we have all the whites in the row make remaining squares blue
                    elif whiteCountRow == self.size / 2 and blueCountRow != self.size / 2:
                        for i in range(self.size):
                            if self.board[a][i] == "y":
                                self.board[a][i] = "k"
                    #if we have all the blues in the col make the remaining squares white
                    if blueCountCol == self.size / 2 and whiteCountCol != self.size / 2:
                        for i in range(self.size):
                            if self.board[i][a] == "y":
                                self.board[i][a] = "e"
                    #if we have all the whites in the col make remaining squares blue
                    elif whiteCountCol == self.size / 2 and blueCountCol != self.size / 2:
                        for i in range(self.size):
                            if self.board[i][a] == "y":
                                self.board[i][a] = "k"
                    if whiteCountRow == self.size / 2 and blueCountRow == self.size / 2:
                        if a not in solvedRows:
                            solvedRows.add(a)

    def updateBoard(self):
        count = 0
        for j in range(0, self.size):
            for i in range(0, self.size):
                square = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="square' + str(count) + '"]')))
                if self.board[j][i] == "e":
                    square.click()
                    square.click()
                elif self.board[j][i] == "k":
                    square.click()
                count += 1

for i in range(100):
    print(i)
    newBoard = Board()
    newBoard.makeBoard(14)
    newBoard.solveBoard()
    newBoard.updateBoard()

driver.quit()
