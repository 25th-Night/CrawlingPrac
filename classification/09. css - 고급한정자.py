from bs4 import BeautifulSoup as BS
import requests as req


# multiline string
html = """
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <style>
        table {
            border-collapse: collapse;
            border: 1px solid black;
            margin: 20px 0;
        }

        table td,
        table th {
            border: 1px solid black;
        }

        table tr:first-child th {
            border-top: 0;
        }

        table tr:last-child td {
            border-bottom: 0;
        }

        table tr td:first-child,
        table tr th:first-child {
            border-left: 0;
        }

        table tr td:last-child,
        table tr th:last-child {
            border-right: 0;
        }
    </style>
</head>

<body>
    <div style="max-width: 960px; margin: auto; padding-top: 20px;">
        <h1>패스트 호텔 예약 확인</h1>
        <input type="checkbox">
        <span>이용 약관을 충분히 숙지하였으며 이에 동의합니다.</span>
        <br>
        <input type="checkbox" checked>
        <span>14세 이상 보호자 동행에 동의합니다.</span>
        <br>
        <input type="checkbox" disabled>
        <span>5인 이상 단체 예약입니다.</span>
        <br>
        <div>
            <label>전화번호 :</label>
            <input type="text">
        </div>
        <table>
            <thead>
                <tr>
                    <th>번호</th>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>홍길동1</td>
                    <td>
                        <b>100,000</b>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>홍길동2</td>
                    <td>
                        <b>89,000</b>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>홍길동3</td>
                    <td>
                        <b>77,000</b>
                    </td>
                </tr>
            </tbody>
        </table>
        <br>
        <h3>총 가격</h3>
        <div>
            <b>KRW : </b>
            <b>266,000</b>
        </div>
    </div>
</body>

</html>
"""

soup = BS(html, "html.parser")


# enabled
arr_enabled = soup.select("input:enabled")
print(arr_enabled)
# [<input type="checkbox"/>, <input checked="" type="checkbox"/>, <input type="text"/>]


# checked
arr_checked = soup.select("input:checked")
print(arr_checked)
# [<input checked="" type="checkbox"/>]


# disabled
arr_disabled = soup.select("input:disabled")
print(arr_disabled)
# [<input disabled="" type="checkbox"/>]


# empty
arr_empty = soup.select("input:empty")
print(arr_empty)
# [<input type="checkbox"/>, <input checked="" type="checkbox"/>, <input disabled="" type="checkbox"/>, <input type="text"/>]


# 전화번호 옆의 input 태그 가져오기
arr_phone = soup.select("label+input:empty")
print(arr_phone)
# [<input type="text"/>]


# first-child
arr_first_child = soup.select("b:first-child")
print(arr_first_child)
# [<b>100,000</b>, <b>89,000</b>, <b>77,000</b>, <b>KRW : </b>]


# last-child
arr_last_child = soup.select("table tbody tr:last-child")
print(arr_last_child)
# [<tr> <td>3</td> <td>홍길동3</td> <td><b>77,000</b></td> </tr>]


# first-of-type
arr_first_of_type = soup.select("table tbody td:first-of-type")
print(arr_first_of_type)
# [<td>1</td>, <td>2</td>, <td>3</td>]


# last-of-type
arr_last_of_type = soup.select("table tbody td:last-of-type")
print(arr_last_of_type)
# [<td><b>100,000</b></td>, <td><b>89,000</b></td>, <td><b>77,000</b></td>]


# not
arr_not = soup.select("b:not(:first-child)")
print(arr_not)
# [<b>266,000</b>]


# nth-child
arr_nth_child = soup.select("table tbody tr:nth-child(2)")
print(arr_nth_child)
# [<tr>< td>2</td> <td>홍길동2</td> <td><b>89,000</b></td> </tr>]


# nth-of-type
arr_nth_of_type = soup.select("table tbody tr:nth-of-type(2)")
print(arr_nth_of_type)
# [<tr> <td>2</td> <td>홍길동2</td> <td><b>89,000</b></td> </tr>]