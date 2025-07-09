from openai import OpenAI
import pymysql

def DEEPSEEK_API():
    conn = pymysql.connect(
        host= '127.0.0.1',        # 或 127.0.0.1
        port=3306,
        user= 'root',   # 替换为你的用户名
        password='19232416',# 替换为你的密码
        database='device_monitoring',
        charset='utf8mb4'
    )

    cursor = conn.cursor()

    # 2. 查询最近 20 条数据（按 event_time 排序）
    cursor.execute("""
        SELECT p.device_id, p.voltage, p.current, p.power, p.electricity, p.control_signal, p.event_time
        FROM device_properties p
        JOIN (
            SELECT device_id, DATE_FORMAT(event_time, '%Y-%m-%d %H:00:00') AS hour,
                MIN(event_time) AS first_time
            FROM device_properties
            GROUP BY device_id, hour
            LIMIT 800
        ) t
        ON p.device_id = t.device_id
        AND DATE_FORMAT(p.event_time, '%Y-%m-%d %H:00:00') = t.hour
        AND p.event_time = t.first_time
        ORDER BY p.event_time DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    data_summary = "以下是插座每分钟一条代表性用电记录（共{}条）：\n".format(len(rows))
    for row in rows:
        device_id, voltage, current, power, electricity, control_signal, event_time = row
        state = "开启" if control_signal == 1 else "关闭"
        data_summary += (
            f"- 设备id: {device_id} 时间：{event_time}, 电压：{voltage}V, 电流：{current}A, 功率：{power}W, "
            f"累计电能：{electricity}kWh, 状态：{state}\n"
        )
    # print(data_summary)


    client = OpenAI(api_key="your-key", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一位智能插座用电数据分析专家。用户将提供插座的电压、电流、功率、累计电能、开关状态与时间等信息。你需要分析其用电特征、找出异常或高能耗情况，并提出节能建议，包括是否需要调整使用时段、是否有异常功耗、是否存在长期待机问题等。你的建议中应该包含你读取了多少条数据，时间横跨了多久，逻辑应清晰具体、易于操作。要求给出三点最重要的，字数100字左右，不需要你写出一共有多少字)"},
            {"role": "user", "content": data_summary},
        ],
        stream=False
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content