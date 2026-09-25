from mc.physics.interactions import sample_collision, sample_free_path, scatter 

def transport(particle, geometry, material, rng, tally):

    while particle.alive:

        free_path = sample_free_path(rng, material)

        boundary_distance = geometry.distance_to_boundary(particle)

        if free_path < boundary_distance:

            x_old = particle.x
            particle.x += particle.direction * free_path
            tally.score_track(x_old, particle.x)
            interaction = sample_collision(rng, material)

            if interaction == "absorption":
                particle.alive = False
            else:
                particle.direction = scatter(rng)

        else:
            x_old = particle.x

            particle.x += particle.direction * boundary_distance

            tally.score_track(x_old, particle.x)

            particle.alive = False