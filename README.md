# SESS Web Service

a simple client for communicating with <https://sess.sku.ac.ir> WSDL-SOAP-based web services

## StdService

The following operations are supported.
* GetKey
* Login
* SetList
* GetList

For more details, please review the [web-service docs](https://sess.sku.ac.ir/sess/WebServices/StdService.asmx).

### Gates

### Error Codes


#### GetKey

| Error Code | Detail |
| :--------- | -----: |
| 001        | ‫کاربر وجود ندارد یا مجوز اتصال به وب سرویس را ندارد.‬ |

#### Login

| Error Code | Detail |
| :--------- | -----: |
| 001        | ‫وب سرویس یافت نشد.‬ |
| 002        | ‫کاربر مجوز استفاده از این وب سرویس را ندارد.‬ |
| 064        | ‫شناسه کاربری یا کلمه رمز غلط است.‬ |

#### SetList

| Error Code | Detail |
| :--------- | -----: |
| 001        | ‫کاربر به این وب سرویس وارد نشده است.‬ |
| 002        | ‫کاربر مجوز استفاده از این وب سرویس را ندارد.‬ |
| 003        | ‫عبارت جستجو نباید شامل حروف کنترل باشد.‬ |
| 004        | ‫متن خطای داخلی‬ |
| 064        | ‫شناسه کاربری یا کلمه رمز غلط است.‬ |

#### GetList

| Error Code | Detail |
| :--------- | -----: |
| 001        | ‫کاربر به این وب سرویس وارد نشده است.‬ |
| 002        | ‫کاربر مجوز استفاده از این وب سرویس را ندارد.‬ |
| 003        | ‫عملیات جستجو انجام نشده است.‬ |
| 064        | ‫شناسه کاربری یا کلمه رمز غلط است.‬ |
