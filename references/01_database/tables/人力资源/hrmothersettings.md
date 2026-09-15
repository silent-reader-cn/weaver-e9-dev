# 泛微OA 数据表: `hrmothersettings`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmothersettings`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remindperiod` | 密码变更提醒周期 | `char` | 4 | 是 | 密码变更提醒周期 |
| 2 | `valid` | 密码变更提醒功能是否有效 | `char` | 1 | 是 | 密码变更提醒功能是否有效 |
| 3 | `birthremindperiod` | 生日提醒周期 | `char` | 4 | 是 | 生日提醒周期 |
| 4 | `birthvalid` | 生日提醒功能是否有效 | `char` | 1 | 是 | 生日提醒功能是否有效 |
| 5 | `congratulation` | 贺词 | `varchar2` | 400 | 是 | 贺词 |
| 6 | `birthremindmode` | 提醒方式 | `char` | 1 | 是 | 1、弹出窗口；2、工作流 |
| 7 | `needusb` | 是否usb加密 | `char` | 1 | 是 | 是否usb加密 |
| 8 | `firmcode` | usb加密公司代码 | `char` | 10 | 是 | usb加密公司代码 |
| 9 | `usercode` | usb加密用户代码 | `char` | 10 | 是 | usb加密用户代码 |
| 10 | `relogin` | 是否允许重复登陆 | `char` | 1 | 是 | 是否允许重复登陆 |
| 11 | `needvalidate` | 是否需要验证码 | `integer` | - | 是 | 0：不是，1：是 |
| 12 | `validatetype` | 验证码类型 | `integer` | - | 是 | 0：数字，1：字母，2：汉字 |
| 13 | `validatenum` | 验证码位数 | `integer` | - | 是 | 验证码位数 |
| 14 | `minpasslen` | 最小密码长度 | `integer` | - | 是 | 最小密码长度 |
| 15 | `needdynapass` | 是否需要动态密码 | `integer` | - | 是 | 0：不是，1：是 |
| 16 | `dynapasslen` | 动态密码长度 | `integer` | - | 是 | 动态密码长度 |
