#測試佈署 Flask

步驟：

1. 註冊Heroku帳戶
2. 下載並安裝Heroku CLI
3. 在命令列上，執行heroku login
4. 安裝 git
5. 建立虛擬環境 (VirtualEnv)
6. 安裝必要的套件，寫好程式並測試是否可運行
7. 安裝 gunicorn (Heroku上面需要使用)
8. 建立 runtime.txt (Python直譯器版本)
9. 建立 Procfile (Heroku上面要跑什麼的設定)
10. 建立 requirements.txt (我們安裝了那些套件，什麼版本？)
11. 初始化版本管理 (git init)
12. 將所有檔案加入版本管理系統 (git add .)
13. 將檔案放進檔案管理系統 (git commit -m "版本訊息")
14. heroku create [App名稱] (也可以在Heroku上面設定AppName再用git remote add 加入連結)
15. git push heroku master
