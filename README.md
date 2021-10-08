#測試佈署 Flask

步驟：

註冊Heroku帳戶
下載並安裝Heroku CLI
在命令列上，執行heroku login
安裝 git
建立虛擬環境 (VirtualEnv)
安裝必要的套件，寫好程式並測試是否可運行
安裝 gunicorn (Heroku上面需要使用)
建立 runtime.txt (Python直譯器版本)
建立 Procfile (Heroku上面要跑什麼的設定)
建立 requirements.txt (我們安裝了那些套件，什麼版本？)
初始化版本管理 (git init)
將所有檔案加入版本管理系統 (git add .)
將檔案放進檔案管理系統 (git commit -m "版本訊息")
heroku create [App名稱] (也可以在Heroku上面設定AppName再用git remote add 加入連結)
git push heroku master
