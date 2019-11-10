# trafficsignrecognize
Đồ án nhận diện biển báo cấm đơn trong ảnh môi trường có sử dụng deep learning.<br>

<h2>Yêu cầu:</h2>
<b>Python:</b><br>
<ul>
     <li>python 3.6.9</li>
</ul>
<br>
<b>Packages:</b><br>
<i>*Khuyến khích sử dụng Anaconda 3 để cài tất cả packages</i><br>
<ul>
     <li>django 2.2.5</li>
     <li>cv2 (opencv) 3.4.2</li>
     <li>numpy 1.17.2</li>
     <li>matplotlib 3.1.1</li>
     <li>skimage (scikit-image) 0.15.0</li>
     <li>random</li>
     <li>tensorflow 2.0.0</li>
     <li>keras 2.2.4</li>
     <li>PIL (pillow)</li>
     <li>os</li>
</ul>
<h2>Run project:</h2>
Activate biến môi trường Anaconda 3
<pre>source ospath/anaconda3/anaconda3/bin/activate</pre>
Activate môi trường chứa các packages cần thiết
<pre>conda activate opencv</pre>
Di chuyển đến thư mục chứa project
<pre>cd parentProjectPath/trafficsignrecognize </pre>
Chạy server
<pre>python manage.py runserver</pre><br>
Sau khi chạy server thành công truy cập địa chỉ <a href="http://localhost:8000/" target="_blank">localhost:8000</a> để thao tác.
<hr>
<b>Hỗ trợ các biển báo:</b> (Theo bộ biển báo chuẩn Việt Nam)<br>
<ul>
     <li>101: Đường cấm</li>
     <li>102: Cấm đi ngược chiều</li>
     <li>122: Dừng lại</li>
     <li>127: Tốc độ tối đa cho phép</li>
</ul>
Tham khảo source code train file model.h5 tại <a href="https://github.com/quangkhoiuit98/trainmodeltrafficsignrecognize">github.com/quangkhoiuit98/trainmodeltrafficsignrecognize</a>
<br>
<br>
<h2>Chức năng chính</h2>
<b>Trang chủ</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nhận diện biển báo từ ảnh môi trường<br>
<br>
<img src="https://github.com/quangkhoiuit98/trafficsignrecognize/blob/master/static/image/index1.png"><br>
<br><br>
<img src="https://github.com/quangkhoiuit98/trafficsignrecognize/blob/master/static/image/index2.png"><br>

<b>Trang tra cứu biển báo</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tra cứu biển báo từ dữ liệu của ứng dụng<br><br>

<img src="https://github.com/quangkhoiuit98/trafficsignrecognize/blob/master/static/image/trafficinfomation.png"><br><br>
