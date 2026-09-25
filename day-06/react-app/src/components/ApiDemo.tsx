import useApi from "../hooks/useApi";

interface ApiUser {
    id: number;
    name: string;
    email: string;
}

function ApiDemo() {
    const {
        data: users,
        loading,
        error
    } = useApi<ApiUser[]>(
        "https://jsonplaceholder.typicode.com/users"
    );

    if (loading) {
        return <p>Loading API data...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    return (
        <div>
            <h2>API Integration Demo</h2>

            {users?.map((user) => (
                <p key={user.id}>
                    {user.name} — {user.email}
                </p>
            ))}
        </div>
    );
}

export default ApiDemo;

