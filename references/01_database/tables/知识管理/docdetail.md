# 泛微OA 数据表: `docdetail`

- **所属模块**: `知识管理`
- **数据库表名**: `docdetail`
- **字段总数**: `53`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `sumdownload` | 下载量 | `integer` | - | 是 | - |
| 2 | `accessorycount` | 附件个数 | `integer` | - | 是 | - |
| 3 | `replaydoccount` | 回复文档的数量 | `integer` | - | 是 | - |
| 4 | `usertype` | 用户类型 | `char` | 1 | 是 | 1：人力资源，2：客户 |
| 5 | `docno` | 文档归档号 | `varchar2` | 800 | 是 | - |
| 6 | `cancopy` | 是否可以拷贝 | `char` | 1 | 是 | 1、是；0、否 |
| 7 | `canremind` | 回复是否提醒 | `char` | 1 | 是 | 1、是；0、否 |
| 8 | `countmark` | 打分次数 | `integer` | - | 是 | - |
| 9 | `summark` | 总分数 | `integer` | - | 是 | - |
| 10 | `sumreadcount` | 浏览量 | `integer` | - | 是 | - |
| 11 | `orderable` | 是否可以订阅 | `char` | 1 | 是 | 1、是；0、否 |
| 12 | `docextendname` | 扩展名 | `char` | 10 | 是 | 可选项：doc 、html、xls |
| 13 | `doccode` | 文档编号 | `varchar2` | 1000 | 是 | - |
| 14 | `docedition` | 文档版本 | `integer` | - | 是 | - |
| 15 | `doceditionid` | 文档版本id | `integer` | - | 是 | - |
| 16 | `ishistory` | 是否历史 | `integer` | - | 是 | 1:是，0：否 |
| 17 | `maindoc` | 主文档 | `integer` | - | 是 | - |
| 18 | `approvetype` | 审批类型 | `integer` | - | 是 | 1:生效审批,2:失效审批 |
| 19 | `readoptercanprint` | 允许只读操作人打印 | `integer` | - | 是 | 0:不允许，1:允许 |
| 20 | `docvaliduserid` | 生效操作人 | `integer` | - | 是 | - |
| 21 | `docvaliddate` | 生效日期 | `char` | 10 | 是 | - |
| 22 | `docvalidtime` | 生效时间 | `char` | 8 | 是 | - |
| 23 | `docpubuserid` | 发布操作人 | `integer` | - | 是 | - |
| 24 | `docpubdate` | 发布日期 | `char` | 10 | 是 | - |
| 25 | `docpubtime` | 发布时间 | `char` | 8 | 是 | - |
| 26 | `docreopenuserid` | 重新打开操作人 | `integer` | - | 是 | - |
| 27 | `docreopendate` | 重新打开日期 | `char` | 10 | 是 | - |
| 28 | `docreopentime` | 重新打开时间 | `char` | 8 | 是 | - |
| 29 | `docinvaluserid` | 失效操作人 | `integer` | - | 是 | - |
| 30 | `docinvaldate` | 失效日期 | `char` | 10 | 是 | - |
| 31 | `docinvaltime` | 失效时间 | `char` | 8 | 是 | - |
| 32 | `doccanceluserid` | 作废操作人 | `integer` | - | 是 | - |
| 33 | `doccanceldate` | 作废日期 | `char` | 10 | 是 | - |
| 34 | `doccanceltime` | 作废时间 | `char` | 8 | 是 | - |
| 35 | `selectedpubmouldid` | 选择的发布模板 | `integer` | - | 是 | - |
| 36 | `checkoutstatus` | 签出状态 | `char` | 1 | 是 | 1：自动签出，2：强制签出，0或其它：未签出 |
| 37 | `checkoutuserid` | 签出用户 | `integer` | - | 是 | - |
| 38 | `checkoutusertype` | 签出用户类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 39 | `checkoutdate` | 签出日期 | `char` | 10 | 是 | - |
| 40 | `checkouttime` | 签出时间 | `char` | 8 | 是 | - |
| 41 | `hasusedtemplet` | 是否套红，即是否已经套用显示模板 | `char` | 1 | 是 | 1：已经套红，0或null：尚未套红。针对已经套红的文档将不能调用显示模板或编辑模板。 |
| 42 | `invalidationdate` | 失效日期 | `char` | 10 | 是 | - |
| 43 | `doccreatertype` | 文档创建者类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 44 | `doclastmodusertype` | 文档最后修改者类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 45 | `docapproveusertype` | 文档审批者类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 46 | `docvalidusertype` | 生效操作人类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 47 | `docinvalusertype` | 失效操作人类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 48 | `docarchiveusertype` | 文档归档者类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 49 | `doccancelusertype` | 作废操作人类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 50 | `docpubusertype` | 发布操作人类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 51 | `docreopenusertype` | 重新打开操作人类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 52 | `ownertype` | 文档拥有者类型 | `char` | 1 | 是 | 1:内部用户，2：外部用户 |
| 53 | `docstatus` | 文档状态 | `integer` | - | 是 | - |
