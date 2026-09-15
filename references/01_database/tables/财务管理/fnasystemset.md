# 泛微OA 数据表: `fnasystemset`

- **所属模块**: `财务管理`
- **数据库表名**: `fnasystemset`
- **字段总数**: `42`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `optionalsubject` | 科目浏览按钮可选科目规则 | `integer` | - | 是 | 0：可以选择的科目为开启了可编制预算的科目及其下级科目； 1：末级科目（可编制预算的科目或隶属于某个可编制预算的科目）； |
| 2 | `wfdtlimprole4subject` | 科目字段流程明细导入规则 | `integer` | - | 是 | 0：按名称； 1：按编码； |
| 3 | `wfdtlimprole4fcc` | 成本中心字段流程明细导入规则 | `integer` | - | 是 | 0：按名称； 1：按编码； |
| 4 | `costcontrolcycle` | 费用控制周期 | `integer` | - | 是 | 0：按科目预算周期； 1：按预算年度累计控制； |
| 5 | `timemodul` | 自动结转触发模式 | `integer` | - | 是 | 0:自定义结转周期;1:每天;2:每月; |
| 6 | `daytime1` | 自动结转触发日期1 | `integer` | - | 是 | 数字1~28；表示每月1号~28号 |
| 7 | `fer` | 自动结转触发间隔 | `integer` | - | 是 | 定时任务表达式 |
| 8 | `daytime2` | 自动结转触发日期2 | `integer` | - | 是 | 数字1~23；表示每条1点~23点 |
| 9 | `enabledispalyall` | 选择科目浏览按钮显示所有层级 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 10 | `separator` | 科目浏览按钮显示所有层级时，层级间分隔符 | `varchar2` | 120 | 是 | 分隔符，不允许使用英文半角逗号 |
| 11 | `budgetcontroltype` | 下级独立预算; | `integer` | - | 是 | 1：启用；其他：不启用； |
| 12 | `budgetcontroltype1` | 下级独立预算时是否允许费用超标 | `integer` | - | 是 | 1:不允许费用超标;2:允许费用超标; |
| 13 | `automoveminusamt` | 是否结转超额费用 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 14 | `subjectbrowsedefexpanded` | 单科目浏览框默认展开 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 15 | `enablerptctrl` | 启用报表权限控制 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 16 | `cancelbudgetperiodcheck` | 预算期间关闭时不可使用预算 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 17 | `cancelcostlimitedcheck` | 预算期间关闭时，同时控制在途费用 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 18 | `budgetcontroltype2` | 开启上下级独立预算; | `integer` | - | 是 | 1：启用；其他：不启用； |
| 19 | `subjectcodeuniquectrl` | 科目编码（预算科目编码）校验规则 | `integer` | - | 是 | 0：全局唯一； 1：无唯一性控制； 2：按科目应用范围唯一（分部级/成本中心）； 3：按科目应用范围唯一（部门级/成本中心）； |
| 20 | `subjectcodeuniquectrl2` | 科目编码（会计科目编码）校验规则 | `integer` | - | 是 | 0：全局唯一； 1：无唯一性控制； 2：按科目应用范围唯一（分部级/成本中心）； 3：按科目应用范围唯一（部门级/成本中心）； |
| 21 | `id` | ID | `integer` | - | 是 | - |
| 22 | `ifbudgetmove` | 是否结转设置 | `integer` | - | 是 | 0：否，1：是 |
| 23 | `movetypes` | 结转类型 | `varchar2` | 400 | 是 | 1：月度，2：季度，3：半年度 |
| 24 | `ifbottomtotop` | 是否启用从下至上编辑财务费用设置 | `integer` | - | 是 | 0：否，1：是 |
| 25 | `showhiddensubject` | 显示封存科目 | `char` | 1 | 是 | 1：启用；其他：不启用； |
| 26 | `remark` | 备注 | `varchar2` | 4000 | 是 | - |
| 27 | `enableglobalfnactrl` | 启用费控流程提交校验 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 28 | `alertvalue` | 科目预警值 | `integer` | - | 是 | 整数预算额度百分比换算用 |
| 29 | `agreegap` | 允许偏差 | `integer` | - | 是 | 整数预算额度百分比换算用 |
| 30 | `enableruleset` | 启用预算编制权限 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 31 | `fnabudgetoaorg` | 启用预算编制维度：OA组织机构 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 32 | `fnabudgetcostcenter` | 启用预算编制维度：成本中心 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 33 | `wfforceoverlogic` | 强制归档流程费用业务逻辑 | `integer` | - | 是 | 0：释放冻结预算；1：生效冻结预算； |
| 34 | `cancelfnaeditcheck` | 取消预算编制页面的验证功能 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 35 | `budgetautomovepending` | 是否结转审批中预算 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 36 | `recursivesuborg` | 费用流程中 显示时递归统计下级费用单位的已发生、审批中费用 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 37 | `fnawfsyswf` | 流程允许批量提交 报销申请单;付款申请单 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 38 | `fnawfcustom` | 流程允许批量提交 自定义表单费控流程 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 39 | `subjectfilter` | 科目过滤 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 40 | `fnabackgroundvalidator` | 启用费控流程提交后端校验 | `integer` | - | 是 | 1：启用；其他：不启用； |
| 41 | `ifbudgetmove2` | 作废 | `integer` | - | 是 | - |
| 42 | `ifbudgetmoverepeat` | 作废 | `integer` | - | 是 | - |
