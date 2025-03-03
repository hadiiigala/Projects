import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Database connection setup (replace with your actual MySQL details)
def create_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass@123",
            database="music_album_management_system"
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Connection Error", f"Error connecting to database: {e}")
        return None

# Main application class
class MusicAlbumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Album Management System")
        self.root.geometry("800x600")
        
        # Label and buttons for each table
        Label(self.root, text="Select a Table to Manage", font=("Arial", 18)).pack(pady=10)
        
        Button(self.root, text="Manage Songs", command=self.manage_songs, width=20).pack(pady=5)
        Button(self.root, text="Manage Labels", command=self.manage_labels, width=20).pack(pady=5)
        Button(self.root, text="Manage Movies", command=self.manage_movies, width=20).pack(pady=5)
        Button(self.root, text="Manage Albums", command=self.manage_albums, width=20).pack(pady=5)
        Button(self.root, text="Manage Lyrics", command=self.manage_lyrics, width=20).pack(pady=5)
        Button(self.root, text="Manage Tracks", command=self.manage_tracks, width=20).pack(pady=5)
        Button(self.root, text="Manage Singers", command=self.manage_singers, width=20).pack(pady=5)
        Button(self.root, text="Manage Genres", command=self.manage_genres, width=20).pack(pady=5)
        Button(self.root, text="Manage Composers", command=self.manage_composers, width=20).pack(pady=5)
        Button(self.root, text="Manage Reviews", command=self.manage_reviews, width=20).pack(pady=5)
        Button(self.root, text="Manage Purchases", command=self.manage_purchases, width=20).pack(pady=5)

    # Functions to open management windows for each table
    def manage_songs(self):
        self.manage_table("Song", ["S_id", "S_name", "S_releasedate", "S_language", "S_duration", "L_id"])

    def manage_labels(self):
        self.manage_table("Label", ["L_id", "L_legacy", "L_count", "L_name"])

    def manage_movies(self):
        self.manage_table("Movies", ["M_id", "M_name", "M_duration", "M_location", "L_id"])

    def manage_albums(self):
        self.manage_table("Albums", ["A_id", "A_name", "A_releasedate", "A_NoOfSongs", "S_id"])

    def manage_lyrics(self):
        self.manage_table("Lyrics", ["Ly_rhyme", "Ly_language", "Ly_pov", "S_id"])

    def manage_tracks(self):
        self.manage_table("Tracks", ["T_id", "T_count", "S_id"])

    def manage_singers(self):
        self.manage_table("Singer", ["Si_name", "Si_age", "Si_gender", "Si_rank", "Si_id"])

    def manage_genres(self):
        self.manage_table("Genre", ["G_id", "G_type", "S_id", "Si_id"])

    def manage_composers(self):
        self.manage_table("Composer", ["C_name", "C_age", "C_gender", "C_id"])

    def manage_reviews(self):
        self.manage_table("Reviews", ["R_rating", "R_date", "R_id", "S_id", "G_id", "M_id", "A_id", "P_id", "T_id"])

    def manage_purchases(self):
        self.manage_table("Purchase", ["P_amount", "P_duration", "P_mode", "P_id", "L_id"])

    # General function to manage a table
    def manage_table(self, table_name, columns):
        # Create a new window
        table_window = Toplevel(self.root)
        table_window.title(f"Manage {table_name}")
        
        # Treeview to display records
        tree = ttk.Treeview(table_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill=BOTH, expand=1)
        
        # Database operations
        def load_records():
            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name}")
                records = cursor.fetchall()
                for row in tree.get_children():
                    tree.delete(row)
                for record in records:
                    tree.insert('', 'end', values=record)
                conn.close()
        
        def add_record():
            values = [entry.get() for entry in entries]
            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})", values)
                conn.commit()
                conn.close()
                load_records()
        
        def delete_record():
            selected = tree.selection()
            if selected:
                record = tree.item(selected[0])['values']
                record_id = record[0]
                conn = create_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(f"DELETE FROM {table_name} WHERE {columns[0]} = %s", (record_id,))
                    conn.commit()
                    conn.close()
                    load_records()
        
        def update_record():
            selected = tree.selection()
            if selected:
                record = tree.item(selected[0])['values']
                values = [entry.get() for entry in entries]
                conn = create_connection()
                if conn:
                    cursor = conn.cursor()
                    update_stmt = f"UPDATE {table_name} SET " + ", ".join([f"{col} = %s" for col in columns[1:]]) + f" WHERE {columns[0]} = %s"
                    cursor.execute(update_stmt, values[1:] + [record[0]])
                    conn.commit()
                    conn.close()
                    load_records()
        
        # Entry fields and buttons
        frame = Frame(table_window)
        frame.pack(fill=X)
        entries = []
        for col in columns:
            Label(frame, text=col).pack(side=LEFT, padx=5)
            entry = Entry(frame)
            entry.pack(side=LEFT, padx=5)
            entries.append(entry)

        Button(frame, text="Add", command=add_record).pack(side=LEFT, padx=5)
        Button(frame, text="Delete", command=delete_record).pack(side=LEFT, padx=5)
        Button(frame, text="Update", command=update_record).pack(side=LEFT, padx=5)
        
        # Load records initially
        load_records()

# Run the application
root = Tk()
app = MusicAlbumApp(root)
root.mainloop()
