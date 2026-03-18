export default function Pagination({ currentPage, totalPages, onPageChange }) {
    const pages = [];

    for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
    }

    return (
        <div className="flex justify-center items-center gap-4 mt-10">

            {/* Prev */}
            <button
                onClick={() => onPageChange(currentPage - 1)}
                disabled={currentPage === 1}
                className="px-3 py-1 rounded-[8px] bg-[#E6E6E6] disabled:opacity-50"
            >
                Prev
            </button>

            {/* Numbers */}
            {pages.map((page) => (
                <button
                    key={page}
                    onClick={() => onPageChange(page)}
                    className={`px-3 py-1 rounded-[8px] ${
                        currentPage === page
                            ? "bg-black text-white"
                            : "bg-[#E6E6E6]"
                    }`}
                >
                    {page}
                </button>
            ))}

            {/* Next */}
            <button
                onClick={() => onPageChange(currentPage + 1)}
                disabled={currentPage === totalPages}
                className="px-3 py-1 rounded-[8px] bg-[#E6E6E6] disabled:opacity-50"
            >
                Next
            </button>
        </div>
    );
}

