import React from "react";
import { useProductStore } from "../store/useProductStore";
import { useEffect } from "react";
import { PackageIcon, PlusCircleIcon, RefreshCwIcon } from "lucide-react";
import ProductCard from "../components/ProductCard";
import AddProductModal from "../components/AddProductModal";

function HomePage() {
    const { products, loading, error, fetchProducts } = useProductStore();

    useEffect(() => {
        fetchProducts();
    }, [fetchProducts]);

    return (
        <main className="mx-w-6xl mx-auto px-4 py-8">
            <div className="flex justify-between items-center mb-8">
                <button
                    className="btn btn-primary"
                    onClick={() =>
                        document.getElementById("add-product-modal").showModal()
                    }
                >
                    <PlusCircleIcon className="size-5 mr-2" />
                    Add Product
                </button>
                <button
                    className="btn btn-ghost btn-circle"
                    onClick={fetchProducts}
                >
                    <RefreshCwIcon className="size-5" />
                </button>
            </div>

            <AddProductModal />

            {error && <div className="alert alert-error mb-8">{error}</div>}

            {products.length === 0 && !loading && (
                <div className="flex flex-col justify-center items-center h-96 space-y-4">
                    <div className="bg-base-100 rounded-full p-6">
                        <PackageIcon className="size-12" />
                    </div>
                    <div className="text-center space-y-2">
                        <h3 className="text-2xl font-semibold ">
                            No products found
                        </h3>
                        <p className="text-gray-500 max-w-sm">
                            Get started by adding your first product to the
                            inventory
                        </p>
                    </div>
                </div>
            )}

            {loading ? (
                <div className="flex justify-center items-center h-64">
                    <div className="loading loading-spinner loading-lg" />
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {products.map((product) => (
                        <ProductCard key={product.id} product={product} />
                    ))}
                </div>
            )}
        </main>
    );
}

export default HomePage;
