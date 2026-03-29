import { users } from "../route";

export async function GET(_request: Request, { params }: { params: { id: string } }) {
    const { id } = await params;
    const user = users.find(user => user.id === parseInt(id));
    return Response.json(user);    
}

export async function PUT(_request: Request, { params }: { params: { id: string } }) {
    const { id } = await params;
    const userIndex = users.findIndex(user => user.id === parseInt(id));
    if (userIndex === -1) {
        return new Response("User not found", { status: 404 });
    }
    const updatedUser = await _request.json();
    users[userIndex] = { id: parseInt(id), name: updatedUser.name };
    return Response.json(users[userIndex]);
    
}

export async function PATCH(_request: Request, { params }: { params: { id: string } }) {
    const { id } = await params;
    const userIndex = users.findIndex(user => user.id === parseInt(id));
    if (userIndex === -1) {
        return new Response("User not found", { status: 404 });
    }
    const updatedUser = await _request.json();
    users[userIndex] = { ...users[userIndex], ...updatedUser };
    return Response.json(users[userIndex]);
}
    

export async function DELETE(_request: Request, { params }: { params: { id: string } }) {
    const { id } = await params;
    const userIndex = users.findIndex(user => user.id === parseInt(id));
    if (userIndex === -1) {
        return new Response("User not found", { status: 404 });
    }
    users.splice(userIndex, 1);
    return new Response(null, { status: 204 });
    
}
