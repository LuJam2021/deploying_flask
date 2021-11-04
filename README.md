#測試佈署 Flask

pip install dj-database-url gunicorn dj-static

  *dj-database-url：heroku處理資料庫的套件
  *gunicorn：heroku伺服器的處理套件
  *dj-static：heroku處理靜態檔案的套件

步驟：

1. 註冊Heroku帳戶
2. 下載並安裝Heroku CLI
3. 在命令列上，執行heroku login
4. 安裝 git
5. 建立虛擬環境 (VirtualEnv)
6. 安裝必要的套件，寫好程式並測試是否可運行
7. pip install gunicorn (Heroku上面需要使用)
8. 建立 runtime.txt (Python直譯器版本) python-3.8.5 OK
9. 建立 Procfile (Heroku上面要跑什麼的設定) web:gunicorn app:app
10. pip freeze > requirements.txt     建立 requirements.txt (我們安裝了那些套件，什麼版本？) 
11. git init                          初始化版本管理
12. git add .                         所有檔案加入版本管理系統
13. git commit -m "訊息"              將檔案放進檔案管理系統
14. heroku create [App名稱]           創立域名(也可以在Heroku上面設定AppName再用git remote add 加入連結)
15. git push heroku master            
16.
17. 如果出現error: failed to push some refs to 'https://git.heroku.com/XXXXX.git' 先查詢 git log 是否有多個版本commit
18. 執行 git reset --hard "HEAD^"  刪除最近的一個版本commit
19. CERT_HAS_EXPIRED: certificate has expired  憑證過期 解決辦法 https://devcenter.heroku.com/articles/keys 測試後仍未解
