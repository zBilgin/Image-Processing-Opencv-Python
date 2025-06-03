# NumPy Fonksiyonları / NumPy Functions

| Fonksiyon / Function Name | Kullanım / Usage            | Açıklama / Description                                         |
|---------------------------|----------------------------|----------------------------------------------------------------|
| `np.arange()`             | `np.arange(start, stop, step)` | Verilen aralıkta eşit adımlarla sayılardan oluşan dizi oluşturur. / Creates an array with evenly spaced values within a given interval. |
| `np.linspace()`           | `np.linspace(start, stop, num)` | Başlangıç ve bitiş arasında eşit aralıklarla belirtilen sayıda eleman üretir. / Generates specified number of evenly spaced elements between start and stop. |
| `np.ones()`               | `np.ones(shape)`            | Tüm elemanları 1 olan dizi oluşturur. / Creates an array filled with ones. |
| `np.zeros()`              | `np.zeros(shape)`           | Tüm elemanları 0 olan dizi oluşturur. / Creates an array filled with zeros. |
| `np.full()`               | `np.full(shape, value)`     | Tüm elemanları belirtilen değer olan dizi oluşturur. / Creates an array filled with specified value. |
| `np.identity()`           | `np.identity(n)`            | Birim matris oluşturur. / Creates an identity matrix. |
| `np.reshape()`            | `np.reshape(arr, new_shape)`| Dizinin boyutunu değiştirir. / Reshapes the array without changing data. |
| `np.copy()`               | `np.copy(arr)`              | Derin kopya oluşturur. / Creates a deep copy of the array. |
| `np.add()`                | `np.add(a, b)`              | İki diziyi eleman bazında toplar. / Element-wise addition of two arrays. |
| `np.subtract()`           | `np.subtract(a, b)`         | İki diziyi eleman bazında çıkarır. / Element-wise subtraction of two arrays. |
| `np.multiply()`           | `np.multiply(a, b)`         | İki diziyi eleman bazında çarpar. / Element-wise multiplication of two arrays. |
| `np.divide()`             | `np.divide(a, b)`           | İki diziyi eleman bazında böler. / Element-wise division of two arrays. |
| `np.dot()`                | `np.dot(a, b)`              | İki dizinin skaler çarpımını hesaplar. / Dot product of two arrays. |
| `np.where()`              | `np.where(condition, x, y)` | Koşul doğruysa 'x', değilse 'y' döner. / Returns x if condition is true, else y. |
| `np.any()`                | `np.any(arr)`               | Dizi içinde herhangi bir öğe True ise True döner. / Returns True if any element is True. |
| `np.all()`                | `np.all(arr)`               | Dizi içindeki tüm öğeler True ise True döner. / Returns True if all elements are True. |
| `np.logical_and()`        | `np.logical_and(a, b)`      | Mantıksal VE işlemi yapar. / Logical AND operation on arrays. |
| `np.logical_or()`         | `np.logical_or(a, b)`       | Mantıksal VEYA işlemi yapar. / Logical OR operation on arrays. |
| `np.shape()`              | `np.shape(arr)`             | Dizinin boyut bilgisini verir. / Returns the shape of the array. |
| `np.size()`               | `np.size(arr)`              | Dizinin toplam eleman sayısını verir. / Returns total number of elements. |
| `np.ndim()`               | `np.ndim(arr)`              | Dizinin boyut sayısını verir. / Returns number of dimensions. |
| `np.sort()`               | `np.sort(arr)`              | Diziyi sıralar. / Sorts the array. |
| `np.unique()`             | `np.unique(arr)`            | Benzersiz öğeleri döner. / Returns unique elements. |
| `np.sum()`                | `np.sum(arr)`               | Elemanların toplamını döner. / Returns sum of elements. |
| `np.mean()`               | `np.mean(arr)`              | Ortalama değerini döner. / Returns mean value. |
| `np.std()`                | `np.std(arr)`               | Standart sapmayı döner. / Returns standard deviation. |
