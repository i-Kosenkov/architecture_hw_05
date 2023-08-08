import boundary_control_entity.presentation
import boundary_control_entity.domain

// Класс, реализующий хранилище книг с использованием коллекций
class BookStore {
    private List<Book> books;

    public BookStore() {
        books = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void removeBook(Book book) {
        books.remove(book);
    }

    public List<Book> getAllBooks() {
        return books;
    }
}