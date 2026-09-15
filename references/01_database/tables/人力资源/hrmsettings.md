# 泛微OA 数据表: `hrmsettings`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsettings`
- **字段总数**: `86`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `congratulation` | 生日祝词 | `varchar2` | 4000 | 是 | - |
| 2 | `usercode` | 用户代码 | `varchar2` | 800 | 是 | - |
| 3 | `brithalarmscope` | 提醒范围 | `varchar2` | 800 | 是 | - |
| 4 | `congratulation1` | 生日祝词(弹窗) | `varchar2` | 4000 | 是 | - |
| 5 | `validitysec` | 动态密码保护有效期（秒） | `varchar2` | 800 | 是 | - |
| 6 | `needusbdefaultht` | 是否需要海泰key登录设置 | `varchar2` | 800 | 是 | - |
| 7 | `birthvalid` | 是否提醒（员工） | `varchar2` | 800 | 是 | - |
| 8 | `passwordcomplexity` | 密码复杂度 | `varchar2` | 800 | 是 | - |
| 9 | `birthremindperiod` | 提醒提前天数 | `varchar2` | 800 | 是 | - |
| 10 | `mobileshowtype` | 移动电话隐私设置可设置项 | `varchar2` | 800 | 是 | - |
| 11 | `contractvalid` | 是否启用合同到期提醒 | `varchar2` | 800 | 是 | - |
| 12 | `validatetype` | 生效类型 | `varchar2` | 800 | 是 | - |
| 13 | `mobileshowtypedefault` | 移动电话隐私设置默认启用方式 | `varchar2` | 800 | 是 | - |
| 14 | `needusbnetwork` | 是否需要网段策略登录设置 | `varchar2` | 800 | 是 | - |
| 15 | `mobileshowset` | 移动电话隐私设置是否允许个人设置 | `varchar2` | 800 | 是 | - |
| 16 | `firmcode` | 验证码 | `varchar2` | 800 | 是 | - |
| 17 | `dynapasslen` | 动态密码长度 | `varchar2` | 800 | 是 | - |
| 18 | `needdynapassdefault` | 是否开启动态密码默认设置 | `varchar2` | 800 | 是 | - |
| 19 | `canmodifydactylogram` | 是否允许客户端修改指纹 | `varchar2` | 800 | 是 | - |
| 20 | `usbtype` | 登录方式类型 | `varchar2` | 800 | 是 | 海泰key：2，动态令牌：3，动态密码：4 |
| 21 | `numvalidatewrong` | 输入密码错误累计次数设置 | `varchar2` | 800 | 是 | - |
| 22 | `dypadcon` | 动态密码图标 | `varchar2` | 800 | 是 | - |
| 23 | `loginmustuppswd` | 首次登录必须修改密码 | `varchar2` | 800 | 是 | - |
| 24 | `relogin` | 重新登录 | `varchar2` | 800 | 是 | - |
| 25 | `checkunjob` | 非在职人员信息查看控制 | `varchar2` | 800 | 是 | 非在职人员信息查看控制，启用后，只有有“离职人员查看”权限的用户才能检索非在职人员 |
| 26 | `openpasswordlock` | 是否开启密码锁定 | `varchar2` | 800 | 是 | - |
| 27 | `valid` | 是否生效设置 | `varchar2` | 800 | 是 | - |
| 28 | `brithalarmadminscope` | 提醒范围（管理员） | `varchar2` | 800 | 是 | - |
| 29 | `minpasslen` | 最小密码长度 | `varchar2` | 800 | 是 | - |
| 30 | `changepassworddays` | 强制密码修改天数 | `varchar2` | 800 | 是 | - |
| 31 | `contractremindperiod` | 提前几天提醒 | `varchar2` | 800 | 是 | - |
| 32 | `daystoremind` | 密码修改提醒提前天数 | `varchar2` | 800 | 是 | - |
| 33 | `checkkey` | 外部用户接口校验码 | `varchar2` | 800 | 是 | - |
| 34 | `enterremindperiod` | 入职提醒时间 | `varchar2` | 800 | 是 | - |
| 35 | `needvalidate` | 是否开启 | `varchar2` | 800 | 是 | - |
| 36 | `validatenum` | 有效次数 | `varchar2` | 800 | 是 | - |
| 37 | `remindperiod` | 提醒时间 | `varchar2` | 800 | 是 | - |
| 38 | `forbidlogin` | 禁止在网段外登录设置 | `varchar2` | 800 | 是 | - |
| 39 | `birthvalidadmin` | 是否提醒（管理员） | `varchar2` | 800 | 是 | - |
| 40 | `needdactylogram` | 是否需要使用维尔指纹验证设备登录认证功能 | `varchar2` | 800 | 是 | - |
| 41 | `needusbdefaultdt` | 动态令牌默认启用方式设置 | `varchar2` | 800 | 是 | - |
| 42 | `needusb` | 动态设置 | `varchar2` | 800 | 是 | - |
| 43 | `passwordchangereminder` | 是否启用密码强制修改 | `varchar2` | 800 | 是 | - |
| 44 | `sumpasswordlock` | 锁定密码错误次数 | `varchar2` | 800 | 是 | - |
| 45 | `birthshowfield` | 显示字段 | `varchar2` | 800 | 是 | - |
| 46 | `entervalid` | 是否启用入职提醒 | `varchar2` | 800 | 是 | - |
| 47 | `needusbht` | 海泰key | `varchar2` | 800 | 是 | - |
| 48 | `statuswithcontract` | 合同状态 | `varchar2` | 800 | 是 | 合同到期后自动将人员置为“无效”状态 |
| 49 | `needusbdefault` | 动态登录默认设置方式 | `varchar2` | 800 | 是 | - |
| 50 | `birthdialogstyle` | 弹窗样式 | `varchar2` | 800 | 是 | - |
| 51 | `needusbdt` | 动态令牌 | `varchar2` | 800 | 是 | - |
| 52 | `birthremindmode` | 生日提醒方式 | `varchar2` | 800 | 是 | - |
| 53 | `needdynapass` | 是否需要动态密码 | `varchar2` | 800 | 是 | - |
| 54 | `defaultresult` | 默认结果 | `varchar2` | 800 | 是 | - |
| 55 | `defaulttree` | 默认数树结构 | `varchar2` | 800 | 是 | - |
| 56 | `birthshowfieldcolor` | 生日显示字段颜色设置 | `varchar2` | 800 | 是 | - |
| 57 | `birthshowcontentcolor` | 生日祝词字体颜色设置 | `varchar2` | 800 | 是 | - |
| 58 | `birthshowfieldwf` | 生日祝词 | `varchar2` | 800 | 是 | - |
| 59 | `checksysvalidate` | 系统信息批量设置验证码控制 | `varchar2` | 800 | 是 | 系统信息批量设置验证码控制 启用后，系统信息批量设置保存的时候需要输入验证码 |
| 60 | `mobilescanca` | 手机CA验证 | `varchar2` | 80 | 是 | - |
| 61 | `needca` | 是否需要CA | `varchar2` | 80 | 是 | - |
| 62 | `needcadefault` | CA默认设置 | `varchar2` | 80 | 是 | - |
| 63 | `cetificatepath` | 证书路径 | `varchar2` | 1000 | 是 | - |
| 64 | `entrydialogstyle` | 入职一周年提醒设置弹窗图片 | `varchar2` | 400 | 是 | - |
| 65 | `entryvalid` | 入职一周年提醒是否开启提醒 | `varchar2` | 400 | 是 | - |
| 66 | `entrycongrats` | 入职一周年提醒祝福词（弹窗提醒） | `varchar2` | 1000 | 是 | - |
| 67 | `entrycongratscolor` | 入职一周年提醒祝福词颜色 | `varchar2` | 400 | 是 | - |
| 68 | `entryfont` | 入职一周年提醒字体 | `varchar2` | 400 | 是 | - |
| 69 | `entryfontsize` | 入职一周年提醒字体大小 | `varchar2` | 400 | 是 | - |
| 70 | `needpasswordlockmin` | 是否开启密码锁定 | `varchar2` | 800 | 是 | - |
| 71 | `passwordlockmin` | 密码锁定分钟数 | `varchar2` | 800 | 是 | - |
| 72 | `needforgotpassword` | 忘记密码开关 | `varchar2` | 1000 | 是 | - |
| 73 | `forgotpasswordmode` | 忘记密码类型设置 | `varchar2` | 1000 | 是 | - |
| 74 | `secondneeddynapass` | 动态密码允许作为二次身份校验 | `integer` | - | 是 | - |
| 75 | `seconddynapassvaliditymin` | 动态密码免密时间(分钟) | `integer` | - | 是 | - |
| 76 | `secondneedusbdt` | 动态令牌允许作为二次身份校验 | `integer` | - | 是 | - |
| 77 | `secondvaliditydtmin` | 动态令牌免密时间(分钟) | `integer` | - | 是 | - |
| 78 | `secondpassword` | 密码允许作为二次身份校验 | `integer` | - | 是 | - |
| 79 | `secondpasswordmin` | 密码免密时间(分钟) | `integer` | - | 是 | - |
| 80 | `addressca` | CA云服务地址 | `varchar2` | 100 | 是 | - |
| 81 | `cadefault` | CA默认启用方式 | `integer` | - | 是 | - |
| 82 | `secondca` | CA允许作为二次身份校验 | `integer` | - | 是 | - |
| 83 | `secondvaliditycamin` | CA免密时间(分钟) | `integer` | - | 是 | - |
| 84 | `addresscl` | 契约锁云服务地址 | `varchar2` | 100 | 是 | - |
| 85 | `secondcl` | 契约锁允许作为二次身份校验 | `integer` | - | 是 | - |
| 86 | `secondvalidityclmin` | 契约锁免密时间(分钟) | `integer` | - | 是 | - |
