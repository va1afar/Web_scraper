# Web_Scraper

## **_Summary_**

-   このアプリは **ウェブサイトの情報を収取するアプリ**です。Python、BeautifulSoup、Selenium、Flask、Pico CSSを使用しました。

    _(This project is **Website Information Collection Application** developed using Python, BeautifulSoup, Selenium, Flask and Pico CSS.)_

-   Medium Blog : [https://medium.com/@va1afar.biz](https://medium.com/@va1afar.biz)

---

## _1. 使用した技術_

-   Language : `Python`

-   Framework : `Flask`

-   Styling : `Pico CSS`

-   Others : `BeautifulSoup`, `Selenium`, `HTML`

---

## _2. アプリの詳細_

- このアプリは

    IndeedKR : [https://kr.indeed.com/](https://kr.indeed.com/)

    WeWorkRemotely : [https://weworkremotely.com/](https://weworkremotely.com/)

    から情報を収取し、.csvファイルとして保存します。
    
    _(This app collects information from [IndeedKR], [WeWorkRemotely] and stores it as a .csv file.)_   

- サイトたちに必要以上のトラフィックを発生させないために、検索する情報の最大値を設定しました。

    _(I set the maximum value of information to search for in order not to cause too much traffic to the sites.)_

- より簡単に使用するために、Flask、Pico CSSを使いUIを改善しました。

    _(Improved UI using Flask and Pico CSS for easier use.)_

- 同じ検索をする場合、もう一度検索する代わりコード内部に保存した情報で直ぐに応答できます。

     _(When user search same keyword, it can immediately respond with the stored information inside the code instead of searching again.)_
