# 泛微OA (E-Cology 9) 消息中心与第三方推送开发指南

> **来源**：泛微云商店官方文档库 (E-CloudStore)
> **功能**：E9 标准消息推送、第三方系统向 OA 推送消息、消息状态变更与待办通知

---


# E9二开、第三方系统推送消息
## E9二开、第三方系统推送消息 KB1908以后
### 一、二开通过调用java源码推送消息：
#### 1、发送消息：
```java


    import com.cloudstore.dev.api.bean.MessageBean;
    import com.cloudstore.dev.api.bean.MessageType;
    import com.cloudstore.dev.api.util.Util_Message;
    
    import java.io.IOException;
    import java.util.HashSet;
    import java.util.Set;
    MessageType messageType = MessageType.newInstance(121); //消息来源（见文档第四点补充）
    Set<String> userIdList = new HashSet<>(); //接收人id
    String title = "标题"; //标题
    String context = "内容"; //内容
    String linkUrl = "PC端链接"; //PC端链接 纯文本就传空字符串
    String linkMobileUrl = "移动端链接"; //移动端链接 纯文本就传空字符串
    try {
       MessageBean messageBean = Util_Message.createMessage(messageType, userIdList, title, context, linkUrl, linkMobileUrl);
       messageBean.setCreater(1);//创建人id
    //message.setBizState("0");需要修改消息状态时传入,表示消息最初状态为待处理
       // messageBean.setTargetId("121|22"); //消息来源code +“|”+业务id  需要修改消息状态时传入，这个字段是自定义的，和修改消息状态的时候传入相同的值，可做更新。
       Util_Message.store(messageBean);
       } catch (IOException e) {
         e.printStackTrace();
   }
```
#### 2、修改消息业务状态：
```java
import com.cloudstore.dev.api.bean.MessageBean;
import com.cloudstore.dev.api.bean.MessageType;
import com.cloudstore.dev.api.util.Util_Message;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
try {
   MessageBean messageBean = Util_Message.createMessage();
   messageBean.setUserList(new HashSet<>());//接收人id
   messageBean.setTargetId("121|22"); targetId code +“|”+业务id删除消息时所依据的条件
   messageBean.setBizState("bizState"); //bizState 业务状态 待处理 0 已处理 1 已同意 2 已拒绝 3 已删除 27 已暂停 34 已撤销 35
     //messageBean.setMessageType(MessageType.newInstance(121));//消息来源code(传了代表code也做为修改时的条件，默认不传）
   Util_Message.updateBizState(messageBean);
   } catch (Exception e) {
     e.printStackTrace();
   }
```
#### 3、删除消息：
```java
import com.cloudstore.dev.api.bean.MessageBean;
import com.cloudstore.dev.api.bean.MessageType;
import com.cloudstore.dev.api.util.Util_Message;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

try {
MessageBean messageBean = Util_Message.createMessage();
messageBean.setUserList(new HashSet<>());//接收人id
messageBean.setTargetId("121|22"); //code + “|” + 业务id，和发消息的targetid一致
//messageBean.setMessageType(MessageType.newInstance(121));//消息来源code(传了代表code也做为删除时的条件，默认不传）
Util_Message.delMessageTargetid(messageBean);
} catch (Exception e) {
e.printStackTrace();
}
}
```
### 二、第三方调用HTTP接口推送消息：
`（ECKB1912之后才支持）`
#### 前提条件以及准备工作
##### （1）、OA-KB检查
		OA系统KB务必在1912之后`
##### （2）、OA数据库插入第三方系统标识
```sql
INSERT  INTO ECOLOGY_BIZ_EC(ID,APPID,NAME) VALUES('123456','5583bc0e-220e-4a44-8e14-d838d47ad9b6','上海泛微网络科技股份有限公司')
```
|字段   |必填   |类型   |说明   |
| ------------ | ------------ | ------------ | ------------ |
| ID  | 是  | String  | 主键id保证唯一即可  |
|  APPID | 是  |  String | 随机字符串，保证唯一即可，在发消息的时候需要传入。 建议使用javaUUID。可访问 http://www.uuid.online/ 生成  |
|  NAME |  是 | String  | 	第三方系统名称  |
##### （3）、清除缓存
`chrome浏览器访问 OA地址/commcache/cacheMonitor.jsp界面，点击重启加载配置，刷新缓存`
##### （4）、修改配置文件
`ecology/WEB-INF/web.xml修改，将EMFilter添加在SessionFilter（或者SessionCloudFilter）之前（已经有了不需要再做修改）`
 ```xml
<filter>
 <filter-name>EMFilter</filter-name>
 <filter-class>com.cloudstore.dev.api.service.EMFilter</filter-class>
 </filter>
 <filter-mapping>
 <filter-name>EMFilter</filter-name>
 <url-pattern>/*</url-pattern>
 </filter-mapping>
 <filter>
 <filter-name>SessionFilter</filter-name>
 <filter-class>com.cloudstore.dev.api.service.SessionFilter</filter-class>
 </filter>
 <filter-mapping>
 <filter-name>SessionFilter</filter-name>
 <url-pattern>/api/*</url-pattern>
 </filter-mapping>
 <filter-mapping>
 <filter-name>SessionFilter</filter-name>
 <url-pattern>/page/interfaces/*.jsp</url-pattern>
 </filter-mapping>
```
##### （5）、重启OA系统
##### （6）、新建自定义消息来源
##### （7）、第三方引入Jar包文件
`在ecology目录中找到ecology/WEB-INF/lib/RSA-0.0.1-SNAPSHOT.jar文件引入到第三方系统项目资源目录下`
#### 1、发送消息：
`tips:（接口有token验证，不可直接调用，具体调用请看下面第4点示例）`
```java
接口：http://OA地址/api/ec/dev/message/sendCustomMessageSingle
请求方式 ： POST
```
| 参数名  |必选   |类型   |说明   |
| ------------ | ------------ | ------------ | ------------ |
|code   | 	是  | string  | 消息来源（见文档第四点补充）  |
| userIdList/loginIdList/workCodeList/lastNameList  |  	是 | string  | 接收人OA系统id/登录名/编号/接收人姓名 （任选一个填入即可，以逗号分隔）  |
| creater  | 否  | string  |  创建人 OA系统id/登录名/编号/姓名（对应接收人所传入的形式） |
| title  | 否  | string  | 	标题  |
| context  |  否 |  string |内容   |
| linkUrl  | 否  |  string |  PC端链接|
| linkMobileUrl  |  否 | string  |移动端链接   |
| targetId | 否  |  string |消息来源code+竖杠+业务ID,需要修改消息时传入,业务ID自定义,是用于修改消息的一个条件  |
| bizState  |  否 | string  | 	0 表示消息初始状态是待处理 需要修改消息状态时传入  |

#### 2、修改消息业务状态：
`tips:（接口有token验证，不可直接调用，具体调用请看下面第4点示例）`
```java
接口：http://OA地址/api/ec/dev/message/alterCustomMessageSingle
请求方式: POST
```
| 参数名  |  必选 | 类型  | 说明  |
| ------------ | ------------ | ------------ | ------------ |
| targetId  |  是 | string  |  消息来源code+竖杠+业务id 修改消息状态时所依据的条件 |
| userIdList/loginIdList/workCodeList/lastNameList  | 是 | string  | 接收人OA系统id/登录名/编号/接收人姓名 （任选一个填入即可，以逗号分隔）
  |
| bizState  |是   | string  | 	业务状态 待处理 0 已处理 1 已同意 2 已拒绝 3 已删除 27 已暂停 34 已撤销 35  |
| code  | 否  | string  | 	消息来源code(传了代表code也做为修改时的条件，默认不传）  |


#### 3、删除消息：
`tips:（接口有token验证，不可直接调用，具体调用请看下面第4点示例）`
```java
接口：http://OA地址/api/ec/dev/message/deleteCustomMessageSingle
请求方式：POST
```

|参数名	   | 必选  |类型   |说明   |
| ------------ | ------------ | ------------ | ------------ |
|targetId   |  是	 |string   | 	消息来源code+竖杠+业务id 删除消息时所依据的条件  |
|  userIdList/loginIdList/workCodeList/lastNameList	 |  是	 |string   | 接收人OA系统id/登录名/编号/接收人姓名 （任选一个填入即可，以逗号分隔）  |
| code  |否   |  string | 	消息来源code(传了代表code也做为删除时的条件，默认不传）  |

#### 4、java调用HTTP接口
`tips:（ECKB1912之后才支持）`

（1）、第三方调用OA系统接口，关于token的相关解释文档：

`https://e-cloudstore.com/doc.html?appId=af09c25938714c26b9736f535ca20fc9`

（2）、新建消息来源（见文档第四点补充，此步骤一定要先去操作）

（3）、调用示例

```java


    import com.alibaba.fastjson.JSON;
    import com.alibaba.fastjson.JSONObject;
    import com.alibaba.fastjson.TypeReference;
    import org.junit.Test;
    import weaver.rsa.security.RSA;
    
    import java.io.*;
    import java.net.HttpURLConnection;
    import java.net.URL;
    import java.security.KeyManagementException;
    import java.security.NoSuchAlgorithmException;
    
    import java.util.Base64;
    import java.util.HashMap;
    import java.util.Map;
    
    /**
     * 1、OA数据库插入
     * INSERT INTO ECOLOGY_BIZ_EC(ID,APPID,NAME) VALUES('123456','5583bc0e-220e-4a44-8e14-d838d47ad9b6','上海泛微网络科技股份有限公司');
     * id 主键保证表中唯一，appid和代码中传入和appid一致，name 名称
     * <p>
     * 2、刷新OAsql缓存
     * chrome浏览器访问 OA地址/commcache/cacheMonitor.jsp界面，点击重启加载配置
     * <p>
     * 3、web.xml修改，将EMFilter添加在SessionFilter之前（已经有了不需要再做修改）
     * <filter>
     * <filter-name>EMFilter</filter-name>
     * <filter-class>com.cloudstore.dev.api.service.EMFilter</filter-class>
     * </filter>
     * <filter-mapping>
     * <filter-name>EMFilter</filter-name>
     * <url-pattern>/*</url-pattern>
     * </filter-mapping>
     * <filter>
     * <filter-name>SessionFilter</filter-name>
     * <filter-class>com.cloudstore.dev.api.service.SessionFilter</filter-class>
     * </filter>
     * <filter-mapping>
     * <filter-name>SessionFilter</filter-name>
     * <url-pattern>/api/*</url-pattern>
     * </filter-mapping>
     * <filter-mapping>
     * <filter-name>SessionFilter</filter-name>
     * <url-pattern>/page/interfaces/*.jsp</url-pattern>
     * </filter-mapping>
     * <p>
     * 4、在ecology系统代码目录中找到ecology/WEB-INF/lib/RSA-0.0.1-SNAPSHOT.jar文件引入到第三方系统项目资源目录下。
     * <p>
     * 以上步骤有所简化，详细对应OA版本的操作步骤请查看文档
     */
    public class MessageTest {
    
        public static void main(String[] args) {
            try {
                testRestful("http://localhost:8080"); //OA地址
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            } catch (KeyManagementException e) {
    
            }
        }
    
        /**
         * APPID 指定一个UUID （请记住是指定一个UUID，作为第三方系统的唯一标识）
         */
        private static final String APPID = "5583bc0e-220e-4a44-8e14-d838d47ad9b6";
    
    
        /**
         * 发送消息，参数封装
         * @return
         */
        public static Map<String,String> sendCustomMessageSingle() {
    
            Map<String, String> map = new HashMap<>();
    
            map.put("code", "559"); // 消息来源,新建消息来源获取code 请查看文档第四大点补充
            map.put("userIdList", "1,3"); // userIdList参数 userIdList 接收人OA系统id / loginIdList 接收人登录名 / workCodeList 接收人编号 / lastNameList 接收人姓名（任选一个填入即可，以逗号分隔）
    //      map.put("loginIdList","zhangsan,wangwu" ); //接收人登录名
    //        map.put("workCodeList","WS01640,WS01641" ); //接收人编号
    //        map.put("lastNameList","张三,王五" ); //接收人姓名
            map.put("creater", "1"); //creater的值 创建人OA系统id / 创建人登录名 / 创建人编号 / 创建人姓名（对应接收人所传入的形式）
    //        map.put("creater","zhangsan");
    //        map.put("creater","WS01640");
    //        map.put("creater","张三");
            map.put("title", "标题");
            map.put("context", "内容");
            map.put("linkUrl", "PC端链接");
            map.put("linkMobileUrl", "移动端链接");
    
    //        map.put("targetId","559|id22"); //消息来源code +“|”+业务id  消息需要打上已处理标记
    //        map.put("bizState","0"); //0 表示消息初始状态是待处理  消息需要打上已处理标记
    
            return map;
        }
    
    
        /**
         * 将消息打上已处理标记，参数封装
         * @return
         */
        public static Map<String,String> alterCustomMessageSingle() {
    
    
            Map<String, String> map = new HashMap<>();
    //        map.put("code","559"); //消息来源code(传了代表，code也要做为修改时where后面的条件）
            map.put("targetId", "559|id22");//修改消息状态时所依据的条件，在消息发送时也需要插入，字符串拼接方式为业务id前加消息来源的“code|"
            map.put("bizState", "1");//待处理 0 已处理 1 已同意 2 已拒绝 3 已删除 27 已暂停 34 已撤销 35
    
            map.put("userIdList", "1,3"); //接收人OA系统id
    //        map.put("loginIdList","zhangsan,wangwu" ); //接收人登录名
    //        map.put("workCodeList","WS01640,WS01641"); //接收人编号
    //        map.put("lastNameList","张三,王五" ); //接收人姓名
    
            return map;
        }
    
    
        /**
         * 删除消息，参数封装
         * @return
         */
        public static Map<String,String> deleteCustomMessageSingle() {
    
            Map<String, String> map = new HashMap<>();
    //        map.put("code","559"); //消息来源code(传了代表，code也要做为修改时where后面的条件）
            map.put("targetId", "559|id22");//修改消息状态时所依据的条件，在消息发送时也需要插入，字符串拼接方式为业务id前加消息来源的“code|"
            map.put("bizState", "1");//待处理 0 已处理 1 已同意 2 已拒绝 3 已删除 27 已暂停 34 已撤销 35
    
            map.put("userIdList", "1,3"); //接收人OA系统id
    //        map.put("loginIdList","zhangsan,wangwu" ); //接收人登录名
    //        map.put("workCodeList","WS01640,WS01641"); //接收人编号
    //        map.put("lastNameList","张三,王五" ); //接收人姓名
    
            return map;
        }
    
    
    
        /**
         * 通过获取到的token请求发消息,修改消息，删除消息接口
         *
         * @param address OA地址
         * @return
         * @throws NoSuchAlgorithmException
         * @throws KeyManagementException
         */
        public static String testRestful(String address) throws NoSuchAlgorithmException, KeyManagementException {
            Map<String, String> heads = new HashMap<>();
            Map<String, Object> datas = testGetoken(address);
            //ECOLOGY返回的token
            String token = (String) (datas.get("token"));
            //封装参数到请求头
            heads.put("appid", APPID);
            heads.put("token", token);
            heads.put("skipsession", "1");
    
            //调用ECOLOGY系统发消息接口，消息推送接口返回为true，代表消息成功加入缓存，实际消息是否发送成功，请查看OA后台消息推送日志，和EM消息日志
            String data = post(address + "/api/ec/dev/message/sendCustomMessageSingle",sendCustomMessageSingle(), heads);
    
            //调用ECOLOGY系统修改消息接口，将消息打上已处理标记
    //        String data = post(address + "/api/ec/dev/message/alterCustomMessageSingle",alterCustomMessageSingle(), heads);
    
            //调用ECOLOGY系统删除消息接口，将消息删除
    //        String data = post(address + "/api/ec/dev/message/deleteCustomMessageSingle",deleteCustomMessageSingle(), heads);
    
    
            System.out.println("testRestful：" + data);
            return data;
        }
    
        /**
         * 通过注册返回的OA系统公钥和秘钥获取token
         *
         * @param address OA地址
         * @return
         * @throws NoSuchAlgorithmException
         * @throws KeyManagementException
         */
        public static Map<String, Object> testGetoken(String address) throws NoSuchAlgorithmException, KeyManagementException {
            Map<String, String> heads = new HashMap<>();
            Map<String, Object> datas = testRegist(address); // 注册接口返回的secrit私钥和spk公钥可以在第一次调用后，第三方系统保存起来，之后调用可以不用再调用这个注册接口
            //ECOLOGY返回的系统公钥
            String spk = (String) (datas.get("spk"));
            RSA rsa = new RSA();
            //对秘钥进行加密传输，防止篡改数据
            String secret = rsa.encrypt(null, (String) (datas.get("secrit")), null, "utf-8", spk, false);
            //封装参数到请求头
            heads.put("appid", APPID);
            heads.put("secret", secret);
            //调用ECOLOGY系统接口进行注册
            String data = post(address + "/api/ec/dev/auth/applytoken",null, heads);
            System.out.println("=====testGetoken=====" + data);
            return JSONObject.parseObject(data, new TypeReference<Map<String, Object>>() {
            });
        }
    
    
        /**
         * 注册第三方系统到OA系统，第一次用APPID获取到公钥spk和私钥secret，第三方系统可以保存，下次不用在请求注册接口
         *
         * @param address OA地址
         * @return
         * @throws NoSuchAlgorithmException
         * @throws KeyManagementException
         */
        public static Map<String, Object> testRegist(String address) throws NoSuchAlgorithmException, KeyManagementException {
            Map<String, String> heads = new HashMap<>();
            //获取当前异构系统RSA加密的公钥
            String cpk = new RSA().getRSA_PUB();
            //封装参数到请求头
            heads.put("appid", APPID);
            heads.put("cpk", cpk);
            //调用ECOLOGY系统接口进行注册
            String data = post(address + "/api/ec/dev/auth/regist",null, heads);
            System.out.println("=====testRegist=====" + data);
            return JSONObject.parseObject(data, new TypeReference<Map<String, Object>>() {
            });
    
        }
    
        /**
         * 此方法仅供参考，第三方系统可采用自己的方式调用http接口
         *
         * @param path 请求路径
         * @param data 请求参数
         * @return
         */
        public static String post(String path, Map<String, String> params, Map<String, String> data) {
            try {
                String str = "";
    
    //            if (params != null) {
    //                StringBuilder stringBuilder = new StringBuilder("?");
    //                for (Map.Entry<String, String> entry : params.entrySet()) {
    //                    stringBuilder.append(entry.getKey()).append("=").append(entry.getValue()).append("&");
    //                }
    //                if (stringBuilder.length() > 1)
    //                    path += stringBuilder.substring(0, stringBuilder.length() - 1);
    //            }
                URL url = new URL(path);
                //打开和url之间的连接
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    //            PrintWriter out = null;
                // 请求参数 编码为 utf-8
                //请求方式
                conn.setRequestMethod("POST");
                //设置通用的请求属性
                conn.setRequestProperty("accept", "*/*");
                conn.setRequestProperty("connection", "Keep-Alive");
                conn.setRequestProperty("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)");
    
                if (data != null)
                    for (Map.Entry<String, String> entry : data.entrySet())
                        conn.setRequestProperty(entry.getKey(), entry.getValue());
    
    
                //设置是否向httpUrlConnection输出，设置是否从httpUrlConnection读入，此外发送post请求必须设置这两个
                //最常用的Http请求无非是get和post，get请求可以获取静态页面，也可以把参数放在URL字串后面，传递给servlet，
                //post与get的 不同之处在于post的参数不是放在URL字串里面，而是放在http请求的正文内。
                conn.setDoOutput(true);
                conn.setDoInput(true);
                OutputStreamWriter out = new OutputStreamWriter(conn.getOutputStream(), "utf-8");
    
                if (params != null)
                    out.write(mapToStr(params));
                //缓冲数据
                out.flush();
    
                out.close();
    
                //获取URLConnection对象对应的输入流
                InputStream is = conn.getInputStream();
                //构造一个字符流缓存
                BufferedReader br = new BufferedReader(new InputStreamReader(is,"utf-8"));
    
                String result = "";
                while ((str = br.readLine()) != null) {
                    result = str;
                }
                //关闭流
                is.close();
                //断开连接，最好写上，disconnect是在底层tcp socket链接空闲时才切断。如果正在被其他线程使用就不切断。
                //固定多线程的话，如果不disconnect，链接会增多，直到收发不出信息。写上disconnect后正常一些。
                conn.disconnect();
                return result;
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }
    
        /**
         * 将Map转换成字符串参数，用于POST GET 请求
         *
         * @param map
         * @return
         */
        public static String mapToStr(Map<String, String> map) {
            StringBuilder stringBuilder = new StringBuilder();
            if (map != null) {
                for (Map.Entry<String, String> entry : map.entrySet()) {
                    stringBuilder.append(entry.getKey());
                    if (entry.getValue() != null)
                        stringBuilder.append("=").append(entry.getValue());
                    stringBuilder.append("&");
                }
            }
            if (stringBuilder.length() > 0)
                return stringBuilder.substring(0, stringBuilder.length() - 1);
            return null;
        }
    }
```
### 三、第三方通过调用Webservice接口推送消息：

------------


先引入Webservice接口，引入webservice方式不是唯一的，具体如何引入可自行百度

（本地项目目录下打开命令行窗口，输入wsimport -s E:\user\workspace\Test\src -keep http://192.168.1.73:8080/services/ServiceMessageCustom?wsdl）

E:\user\workspace\Test\src 本地项目目录

http://192.168.1.73:8080//services/ServiceMessageCustom?wsdl webservice接口（前面是OA地址）

#### 1、发送消息


    注：list可以是OA系统接收人id（userList）、接收人登录名（loginIdList）、接收人编号（workCodeList）、接收人姓名（lastNameList），list中可以存放四种形式的值，对应不同形式的值，参数不同（该调用文件必须和webservice在一个目录下）

```java
import com.alibaba.fastjson.JSON;


import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Test1911 {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        ServiceMessageCustom factory = new ServiceMessageCustom();
        ServiceMessageCustomPortType wsImpl = factory.getServiceMessageCustomHttpPort();
        Map<String,Object> map = new HashMap();
        map.put("code", "61");
        map.put("title", "标题");
        map.put("context", "内容");
        map.put("linkUrl", "PC端链接");
        map.put("linkMobileUrl", "移动端链接");
        // map.put("bizState", "0"); //在消息需要修改状态时传入，表示消息初始的状态是待处理

        // map.put("targetId","code|业务id");// 消息来源code +“|”+业务id  消息需要打上已处理标记

        //可以是OA系统接收人id、接收人登录名、接收人编号、接收人姓名，list中可以存放四种形式的值，对应不同形式的值，参数不同
        Set<String> list = new HashSet();
        list.add("1");
        list.add("3");
//      list.add("sysadmin");
//      list.add("1-汪路军");
//        list.add("杨文元-汪路军");
        map.put("userIdList", list); //接收人OA系统id 第一种形式 参数是userIdList
//      map.put("loginIdList",list ); //接收人登录名 第二种形式 参数是loginIdList
//      map.put("workCodeList",list ); //接收人编号 第三种形式 参数是workCodeList
//      map.put("lastNameList",list ); //接收人姓名 第四种形式 参数是lastNameList

        //对应上面的四种形式，但是参数不变
        map.put("creater", "1"); //创建人OA系统id   第一种形式 参数是creater
//      map.put("creater", "sysadmin");//创建人登录名  第二种形式 参数是creater
//      map.put("creater", "1-汪路军");//创建人编号 第三种形式 参数是creater
//        map.put("creater", "杨文元-汪路军");//创建人姓名 第四种形式 参数是creater

        Map map1 = new HashMap<>();
        Map shareMap = new HashMap<>();
        map1.put("share",shareMap);
        Map extraMap = new HashMap<>();
        extraMap.put("showimage","地址");
        shareMap.put("extra",extraMap);
        map.put("emParams",map1);



        boolean flag =  wsImpl.sendCustomMessageSingle(JSON.toJSONString(map));



    }

}
```
```json
#### 对接企业微信、钉钉的参数：map.put(“emParams”,value);
#### value为发送消息到EM、企业微信、钉钉文档中的（如果有自定义的参数值要传递到企业微信、钉钉，那么可以按照下图中的格式put到emParams参数中，下面的参数不用都写，只写自己想覆盖的值）

{
   "userids": "10|11|12",
   "touser" : "UserID1|UserID2|UserID3",
   "toparty" : "PartyID1|PartyID2",
   "todept" : "DeptID1|DeptID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "share",
   "agentid" : 1,
   "send_type" : 1,
   "send_time" : "",
   "share" : {
        "content" : "新流程测试",
        "extra":{
            "desc" : "描述",
            "showimage":"https://www.e-cology.com.cn/images/p.png",
            "linkurl" : "/common/chatResource/view.jsp?resourcetype=0&resourceid=4876035&isfromchatshare=1&sharer=897",
            "linkurl_pc" : "",
            "opentype" : 1,
            "opentype_pc" : 2,
            "canforward" : 1,
            "callbackurl" : "/api/common/chatResource/addshare?resourcetype=0&resourceid=4876035&isfromchatshare=1&firstSharer=897",
            "sharetypename":"流程"
            "sharetypeicon":"https://www.e-cology.com.cn/images/i.png",
            "sharetypebgcolor":"#FFFFFF",
            "sharetype" : "workflow",
            "shareid" : "4876035"
        },
        "mpTemplateMsgData":{
            "first":{
                "value":"xxxx流程",
                "color":""
            },
            "keyword1":{
                "value":"印鉴管理平台",
                "color":""
            },
            "keyword2":{
                "value":"2019-12-24 18:00:00",
                "color":""
            },
            "remark":{
                "value":"创建人：xxx",
                "color":""
            }
        }
   }
}
```
#### 2、修改消息业务状态：
```java
import com.alibaba.fastjson.JSON;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TestMessage {
    public static void main(String[] args) {
        ServiceMessageCustom factory = new ServiceMessageCustom();
        ServiceMessageCustomPortType wsImpl = factory.getServiceMessageCustomHttpPort();
        Map<String,Object> map = new HashMap<>();
//        map.put("code",121); //消息来源code(传了代表，code也要做为修改时的条件）
        map.put("targetId","121|id22");//修改消息状态时所依据的条件，在消息发送时也需要插入，字符串拼接方式为业务id前加消息来源的“code|"
        map.put("bizState","1");//待处理 0 已处理 1 已同意 2 已拒绝 3 已删除 27 已暂停 34 已撤销 35
        List<String> userList = new ArrayList<>(); //OA系统接收人id、接收人登录名、接收人编号、接收人姓名userList只存放一种接收人的形式，并put到相应的key值中
//        userList.add("1");
        userList.add("sysadmin");
//      userList.add("系统管理员");
//      userList.add("1-汪路军");
//        map.put("userIdList", userList); //接收人OA系统id
        map.put("loginIdList",userList ); //接收人登录名
//      map.put("workCodeList",userList ); //接收人编号
//      map.put("lastNameList",userList ); //接收人姓名

        boolean flag = wsImpl.alterCustomMessageSingle(JSON.toJSONString(map));//修改消息状态
        System.out.println(flag);

    }
}
```
#### 3、删除消息：
```java


    import com.alibaba.fastjson.JSON;
    
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    public class TestMessage {
        public static void main(String[] args) {
            ServiceMessageCustom factory = new ServiceMessageCustom();
            ServiceMessageCustomPortType wsImpl = factory.getServiceMessageCustomHttpPort();
            Map<String,Object> map = new HashMap<>();
    //        map.put("code",121); //消息来源code(传了代表，code也要做为修改时的条件）
            map.put("targetId","121|id22");//修改消息状态时所依据的条件，在消息发送时也需要插入，字符串拼接方式为业务id前加消息来源的“code|"
    
            List<String> userList = new ArrayList<>(); //OA系统接收人id、接收人登录名、接收人编号、接收人姓名userList只存放一种接收人的形式，并put到相应的key值中
    //        userList.add("1");
            userList.add("sysadmin");
    //      userList.add("系统管理员");
    //      userList.add("1-汪路军");
    //        map.put("userIdList", userList); //接收人OA系统id
            map.put("loginIdList",userList ); //接收人登录名
    //      map.put("workCodeList",userList ); //接收人编号
    //      map.put("lastNameList",userList ); //接收人姓名
    
    
            boolean flag = wsImpl.deleteCustomMessageSingle(JSON.toJSONString(map));//删除消息
            System.out.println(flag);
    
    
        }
    }
```
## 四、补充：
#### 1、新建消息来源，生成消息code，用于发消息时传入，作为一类消息的标识
![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059179000.png)

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059186000.png)


#### 2、点击保存并进入详细设置

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059226000.png)

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059234000.png)

#### 3、新建消息类型，选择所新建的消息来源，用于用户接收消息的配置
![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059277000.png)

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059286000.png)

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059291000.png)

#### 4、如果消息需要推送到企业微信、钉钉、云之家，需要将新建的消息类型在EM后台做关联

![](https://e-cloudstore.com/files/ecode/demo/0d084e0145f044d3888b2e16b1875951/f53a26e8397947949ea73bfc8a08f6ea/image/file_1663059319000.png)

